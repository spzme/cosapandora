<?php
$solutions = array(
	// Fotoboek
	'wie dit leest trekt een ad' => 'Goed gedaan, ga naar de volgende locatie om de volgende puzzel op te halen: TODO.',
	// Even verbinden
	'wie de nestor niet eert is de bonus niet weerd' => 'Nee, je moet dit komen vertellen bij de organisatieruimte.'
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