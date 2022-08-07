<?php
    try {
        require('data.php');
        $db = new PDO("pgsql:dbname=$db_name;host=localhost;port=5432;user=$user;password=$password");
    } catch (Exception $e){
        echo "No se pudo conectar a la base de datos: $e";
    }
    try {
        require('data.php');
        $db2 = new PDO("pgsql:dbname=$db_name2;host=localhost;port=5432;user=$user2;password=$password2");
    } catch (Exception $e){
        echo "No se pudo conectar a la base de datos: $e";
    }
?>

