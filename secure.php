<?php
$pdo = new PDO('mysql:host=localhost;dbname=testdb', 'user', 'password');
$stmt = $pdo->prepare('SELECT * FROM products WHERE cat = :cat');
$stmt->execute(['cat' => $_GET['cat']]);
$results = $stmt->fetchAll();
?>
