<?php
// player_api.php

// Verifica se um parâmetro 'server' foi passado na URL
if (isset($_GET['server'])) {
    $server = $_GET['server'];

    // Define os links para os servidores
    $servers = [
        'p2futuro' => 'http://p2futuro.com',
        'voz' => 'http://voz.one'
    ];

    // Verifica se o servidor existe na lista
    if (array_key_exists($server, $servers)) {
        // Redireciona para o link do servidor correspondente
        header("Location: " . $servers[$server]);
        exit();
    } else {
        // Se o servidor não for encontrado, exibe uma mensagem de erro
        echo "Servidor não encontrado.";
    }
} else {
    // Se nenhum parâmetro for passado, exibe uma mensagem de erro
    echo "Nenhum servidor especificado.";
}
?>