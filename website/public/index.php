<?php
$solutions = array(
	// Fotoboek
	'wie dit leest trekt een ad' => 'Goed gedaan, ga naar de volgende locatie om de volgende puzzel op te halen: <tt>52.246482,6.8473261</tt>', // oplossing 13
	// Even verbinden
	'wie de nestor niet eert is de bonus niet weerd' => 'Nee, je moet dit komen vertellen bij de organisatieruimte.', // oplossing 7
	// Morse
	'lsd picknick morgen' => 'Lekker gewerkt pikken. Kijk snel bij de Calslaan op de plek waar Ronnie staat <img src="img/4oianpw.jpeg">', // oplossing 4
	// Twister
	'dagobert duck' => '<tt>52.2418123,6.8488081</tt>', // oplossing 5
	// Elementair
	'sherlock' => 'Goed gedaan, kijk snel op de punt op de UTrack.', // oplossing 10
	// Vlaggen
	'kerel trek buis' => '<tt>52.2447165,6.8460117</tt>', // oplossing 2
	// Lijnen
	'tussen mondriaan en de vlinder' => '<img src="img/11nbioiwa.jpeg">', // oplossing 11
	// Tripverslag
	// oplossingen 1, 3, 6, 8, 9, 12
);

$message = '';

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
	$message = 'Die oplossing is onjuist.';
	$solution = strtolower(trim($_POST['solution']));
	
	if (array_key_exists($solution, $solutions)) {
		$message = $solutions[$solution];
	}
}

echo '<b>Vul in het onderstaande formulier je oplossing in om de volgende puzzel te krijgen:</b><br>';
echo '<form method="post"><input type="text" name="solution"><input type="submit"></form><br>';
echo $message;