<?php
// player_api.php

// Array para armazenar os usuários
$usuarios = [];

// Gera 300 usuários fictícios
for ($i = 1; $i <= 300; $i++) {
    $username = "usuario" . $i; // Nome do usuário
    $password = "senha" . $i;    // Senha correspondente
    $usuarios[] = [
        'username' => $username,
        'password' => $password,
        'type' => 'm3u_plus',
        'stream_url' => "http://cdn4k.live/player_api.php?username=$username&password=$password&type=m3u_plus"
    ];
}

// Cabeçalho para o tipo de arquivo M3U
header("Content-Type: application/vnd.apple.mpegurl");
header("Content-Disposition: attachment; filename=\"playlist.m3u\"");

// Início do arquivo M3U
echo "#EXTM3U\n";

// Adiciona os usuários ao arquivo M3U
foreach ($usuarios as $usuario) {
    echo "#EXTINF:-1, $usuario[username]\n"; // Extensão da informação do stream
    echo $usuario['stream_url'] . "\n";      // URL do stream
}
?>