#! /usr/bin/env python

import copy
import sys

class Game:
	def __init__(self):
		self.finished = False

		self.prev = None
		self.board = Board()

		self.players = [
			NovietPlayer(), 
			FeutPlayer(), 
			SjaarsPlayer(), 
			NulloPlayer()
		]

		self.objects = [
			'groen',
			'blauw',
			'rood',
			'zwart',
			'frikandel',
			'bokkepoot',
			'blik mstr',
			'blik klok'
		]

		self.players[0].left = self.objects[4]
		self.players[0].right = self.objects[2]
		self.players[1].left = self.objects[1]
		self.players[1].right = self.objects[6]
		self.players[2].left = self.objects[7]
		self.players[2].right = self.objects[0]
		self.players[3].left = self.objects[3]
		self.players[3].right = self.objects[5]

		self.board.getCell(1).player = self.players[0]
		self.board.getCell(8).player = self.players[1]
		self.board.getCell(17).player = self.players[2]
		self.board.getCell(24).player = self.players[3]

	def findPlayer(self, player):
		for p in self.players:
			if p.name == player.name:
				return p
		return None

	def turn(self):
		copy_state = copy.deepcopy(self)

		triggerTests = []

		for p in self.players:
			triggerTests.extend(p.testTriggers(self))

		trues = 0
		for t in triggerTests:
			if t:
				trues += 1

		if trues == 1:
			for p in self.players:
				if p.runTriggers(self):
					break
			self.prev = copy_state
		elif trues == 0:
			print('ERROR: No triggers valid')
			print(triggerTests)
			sys.exit()
		else:
			print('ERROR: Multiple triggers valid')
			print(triggerTests)
			sys.exit()

	def finished(self):
		return False

	def __str__(self):
		ret = ''
		ret += str(self.board) + '\n'

		for p in self.players:
			ret += p.name + ' (L = ' + (p.left if p.left else 'none') + ', R = ' + (p.right if p.right else 'none') + ')\n'

		return ret

class Player:
	def __init__(self, name, triggers):
		self.name = name
		self.left = None
		self.right = None
		self.triggers = triggers

	def runTriggers(self, game):
		for trigger in self.triggers:
			if trigger(game):
				self.triggers.remove(trigger)
				return True
		return False

	def getCell(self, game):
		return game.board.findPlayer(self)

	def testTriggers(self, game):
		ret = []

		for trigger in self.triggers:
			ret.append(trigger(game, dry=True))

		return ret

	def __str__(self):
		return self.name

class NovietPlayer(Player):
	def __init__(self):
		super(NovietPlayer, self).__init__('noviet', [self.trigger3, self.trigger9, self.trigger10])

	# In de vorige beurt is er een stift uit je rechterhand gestolen.
	def trigger3(self, game, dry=False):
		triggered = False

		if game.prev:
			if game.prev.findPlayer(self).right != None and self.right == None:
				triggered = True

		# check if dry run
		if dry or not triggered:
			return triggered

		print('Trigger: In de vorige beurt is er een stift uit je rechterhand gestolen.\n')

		self.right = self.left
		self.left = game.board.getCell(8).object
		game.board.getCell(8).object = None

		game.board.getCell(17).letter_color = self.left
		game.board.getCell(17).letter = 'Z'

		game.board.getCell(1).player = None
		game.board.getCell(17).player = self

		return triggered

	# Een student staat op hetzelfde vakje als waar een object ligt.
	def trigger9(self, game, dry=False):
		triggered = False

		for y in range(game.board.size_y):
			for x in range(game.board.size_x):
				if game.board.cells[y][x].object != None and game.board.cells[y][x].player != None:
					triggered = True

		# check if dry run
		if dry or not triggered:
			return triggered

		print('Trigger: Een student staat op hetzelfde vakje als waar een object ligt.\n')

		game.board.getCell(16).object = self.right
		self.right = game.board.getCell(18).object
		game.board.getCell(18).object = None

		game.board.getCell(11).letter_color = self.left
		game.board.getCell(11).letter = 'K'

		game.board.getCell(10).letter_color = self.right
		game.board.getCell(10).letter = 'U'

		game.board.getCell(11).player = None
		game.board.getCell(10).player = self

		return triggered

	# Je hebt in beide handen een stift.
	def trigger10(self, game, dry=False):
		triggered = False

		if self.left in ['zwart', 'blauw', 'rood', 'groen'] and \
			self.right in ['zwart', 'blauw', 'rood', 'groen']:
			triggered = True

		# check if dry run
		if dry or not triggered:
			return triggered

		print('Trigger: Je hebt in beide handen een stift.\n')

		game.board.getCell(15).letter_color = self.left
		game.board.getCell(15).letter = 'D'
		game.board.getCell(13).letter_color = self.right
		game.board.getCell(13).letter = 'D'
		game.board.getCell(19).letter_color = self.left
		game.board.getCell(19).letter = 'D'
		game.board.getCell(23).letter_color = self.right
		game.board.getCell(23).letter = 'D'
		game.board.getCell(24).letter_color = self.left
		game.board.getCell(24).letter = 'D'

		game.board.getCell(10).player = None
		game.board.getCell(24).player = self

		return triggered

class FeutPlayer(Player):
	def __init__(self):
		super(FeutPlayer, self).__init__('feut', [self.trigger2, self.trigger5, self.trigger12])

	# In de vorige beurt is er een student in het vakje onder je komen te staan.
	def trigger2(self, game, dry=False):
		triggered = False

		if game.prev:
			x,y = game.prev.board.findPlayer(self)
			cell = game.prev.board.getCellOrNone(x, y + 1)
			if cell and cell.player == None:
				x,y = game.board.findPlayer(self)
				cell = game.board.getCellOrNone(x, y + 1)
				if cell and cell.player != None:
					triggered = True

		# check if dry run
		if dry or not triggered:
			return triggered

		print('Trigger: In de vorige beurt is er een student in het vakje onder je komen te staan.\n')

		game.board.getCell(8).object = self.left
		self.left = game.board.getCell(1).player.right
		game.board.getCell(1).player.right = None

		game.board.getCell(22).letter_color = self.left
		game.board.getCell(22).letter = 'G'

		game.board.getCell(8).player = None
		game.board.getCell(22).player = self

		return triggered

	# Er ligt iets eetbaars op het speelveld.
	def trigger5(self, game, dry=False):
		triggered = False

		x,y = game.board.findObject(game.objects[4])
		if x and y:
			triggered = True
		x,y = game.board.findObject(game.objects[5])
		if x and y:
			triggered = True

		# check if dry run
		if dry or not triggered:
			return triggered

		print('Trigger: Er ligt iets eetbaars op het speelveld.\n')

		game.board.getCell(11).player = game.board.getCell(17).player
		game.board.getCell(17).player = None
		game.board.getCell(13).player = game.board.getCell(14).player
		game.board.getCell(14).player = None

		game.board.getCell(3).letter_color = self.left
		game.board.getCell(3).letter = 'P'

		game.board.getCell(4).object = self.right
		self.right = None

		game.board.getCell(22).player = None
		game.board.getCell(9).player = self
		game.board.getCell(9).letter_color = self.left
		game.board.getCell(9).letter = 'V'
		game.board.getCell(9).object = None

		return triggered

	# Je staat op dezelfde rij als sjaars.
	def trigger12(self, game, dry=False):
		triggered = False

		_,y = game.board.findPlayer(self)

		found = False
		for x in range(game.board.size_x):
			if game.board.cells[y][x].player and game.board.cells[y][x].player.name == 'sjaars':
				triggered = True
		
		# check if dry run
		if dry or not triggered:
			return triggered

		print('Trigger: Je staat op dezelfde rij als sjaars.\n')

		game.board.getCell(2).letter_color = self.left
		game.board.getCell(2).letter = 'R'

		game.board.getCell(9).player = None
		game.board.getCell(2).player = self

		game.finished = True

		return triggered

class SjaarsPlayer(Player):
	def __init__(self):
		super(SjaarsPlayer, self).__init__('sjaars', [self.trigger1, self.trigger7, self.trigger11])

	# Het collgejaar begint
	def trigger1(self, game, dry=False):
		triggered = False

		if game.prev == None:
			triggered = True

		# check if dry run
		if dry or not triggered:
			return triggered

		print('Trigger: Het collgejaar begint.\n')

		# execute trigger
		game.board.getCell(6).letter_color = self.right
		game.board.getCell(6).letter = 'A'
		game.board.getCell(14).letter_color = self.right
		game.board.getCell(14).letter = 'C'

		game.board.getCell(17).player = None
		game.board.getCell(14).player = self

		return triggered

	# In het vakje boven jou is een letter getekend.
	def trigger7(self, game, dry=False):
		triggered = False

		x,y = game.board.findPlayer(self)
		cell = game.board.getCellOrNone(x, y - 1)
		if cell and cell.letter != None:
			triggered = True

		# check if dry run
		if dry or not triggered:
			return triggered

		print('Trigger: In het vakje boven jou is een letter getekend.\n')

		game.board.getCell(18).object = self.right
		self.right = None
		game.board.getCell(13).player = None
		game.board.getCell(5).player = self

		return triggered

	# Er staat een letter in elk vakje in de kolom waar je in staat.
	def trigger11(self, game, dry=False):
		triggered = False

		x,_ = game.board.findPlayer(self)

		count = 0	
		for y in range(game.board.size_y):
			if game.board.cells[y][x].letter != None:
				count += 1

		if count == 4:
			triggered = True

		# check if dry run
		if dry or not triggered:
			return triggered

		print('Trigger: Er staat een letter in elk vakje in de kolom waar je in staat.\n')

		self.right = game.board.getCell(4).player.left
		game.board.getCell(4).player.left = None

		tmp = game.board.getCell(24).player.left
		game.board.getCell(24).player.left = self.right
		self.right = tmp

		game.board.getCell(18).letter_color = self.right
		game.board.getCell(18).letter = 'T'

		tmp = game.board.getCell(24).player.right
		game.board.getCell(24).player.right = self.right
		self.left = tmp
		self.right = None

		game.board.getCell(12).letter_color = self.left
		game.board.getCell(12).letter = 'W'

		game.board.getCell(5).player = None
		game.board.getCell(12).player = self

		return triggered

class NulloPlayer(Player):
	def __init__(self):
		super(NulloPlayer, self).__init__('nullo', [self.trigger4, self.trigger6, self.trigger8])

	# In een vakje direct diagonaal van je is een blauwe letter getekend.
	def trigger4(self, game, dry=False):
		triggered = False

		# simplified because player starts in bottom right corner
		x,y = game.board.findPlayer(self)
		cell = game.board.getCellOrNone(x - 1, y - 1)
		if cell and cell.letter_color == 'blauw':
			triggered = True

		# check if dry run
		if dry or not triggered:
			return triggered

		print('Trigger: In een vakje direct diagonaal van je is een blauwe letter getekend.\n')

		game.board.getCell(9).object = self.right
		self.right = None

		game.board.getCell(5).letter_color = self.left
		game.board.getCell(5).letter = 'B'
		game.board.getCell(1).letter_color = self.left
		game.board.getCell(1).letter = 'E'

		game.board.getCell(24).player = None
		game.board.getCell(1).player = self

		return triggered

	# In dezelfde kolom als jij staat exact één andere student.
	def trigger6(self, game, dry=False):
		triggered = False

		x,_ = game.board.findPlayer(self)

		count = 0	
		for y in range(game.board.size_y):
			if game.board.cells[y][x].player != None:
				count += 1

		if count == 2:
			triggered = True

		# check if dry run
		if dry or not triggered:
			return triggered

		print('Trigger: In dezelfde kolom als jij staat exact één andere student.\n')

		game.board.getCell(7).letter_color = self.left
		game.board.getCell(7).letter = 'M'
		game.board.getCell(8).letter_color = self.left
		game.board.getCell(8).letter = 'N'
		game.board.getCell(20).letter_color = self.left
		game.board.getCell(20).letter = 'O'
		game.board.getCell(21).letter_color = self.left
		game.board.getCell(21).letter = 'P'

		game.board.getCell(1).player = None
		game.board.getCell(22).player = self

		return triggered

	# Er liggen exact twee objecten op het veld.
	def trigger8(self, game, dry=False):
		triggered = False

		obj_count = 0
		for y in range(game.board.size_y):
			for x in range(game.board.size_x):
				if game.board.cells[y][x].object != None:
					obj_count += 1

		if obj_count == 2:
			triggered = True

		# check if dry run
		if dry or not triggered:
			return triggered

		print('Trigger: Er liggen exact twee objecten op het veld.\n')

		game.board.getCell(4).letter_color = self.left
		game.board.getCell(4).letter = 'Q'
		game.board.getCell(5).player.left = None
		game.board.getCell(22).player = None
		game.board.getCell(4).player = self

		return triggered

class Board:
	def __init__(self):
		self.size_x = 6
		self.size_y = 4
		self.cells = []

		for y in range(self.size_y):
			self.cells.append([])
			for x in range(self.size_x):
				self.cells[-1].append(Cell())

	def findPlayer(self, player):
		for y in range(self.size_y):
			for x in range(self.size_x):
				if self.cells[y][x].player and self.cells[y][x].player.name == player.name:
					return (x, y)

		return (None, None)

	def findObject(self, find_object):
		for y in range(self.size_y):
			for x in range(self.size_x):
				if self.cells[y][x].object == find_object:
					return (x, y)

		return (None, None)

	def getCell(self, n):
		return self.cells[(n - 1) // self.size_x][(n - 1) % self.size_x]

	def getCellOrNone(self, x, y):
		if x >= 0 and y >= 0 and x < self.size_x and y < self.size_y:
			return self.cells[y][x]
		return None

	def __str__(self):
		ret = ''

		for y in range(self.size_y):
			for x in range(self.size_x):
				ret += '[' + str(self.cells[y][x]) + ']'
			ret += '\n'

		return ret

class Cell:
	def __init__(self):
		self.player = None
		self.object = None
		self.letter_color = None
		self.letter = None

	def __str__(self):
		return '{:>6} {:>9} {:1.1} {:1}'.format(
			str(self.player) if self.player else '',
			str(self.object) if self.object else '',
			str(self.letter_color) if self.letter_color else '',
			str(self.letter) if self.letter else ''
		)

if __name__ == '__main__':
	game = Game()
	print('Beginstate.\n')
	print(game)

	while not game.finished:
		game.turn()
		print(game)
