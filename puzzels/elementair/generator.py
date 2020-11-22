#!/usr/bin/env python

from __future__ import print_function

MSG = 'ZORG ERVOOR DAT JE ZO SNEL MOGELIJK HET WOORD SHERLOCK INVULT IN HET ONLINE FORMULIER'

ELEMS = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne',
			'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca',
			'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe']

for c in MSG:
	if c == ' ':
		print(c,end='')
	else:
		print(ELEMS[ord(c) - ord('A')],end='')