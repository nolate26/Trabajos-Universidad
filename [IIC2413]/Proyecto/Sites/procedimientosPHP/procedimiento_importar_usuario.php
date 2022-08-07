<?php

    // Nos conectamos a las bdds
    require("../config/conection.php");
    include('../templates/header.html');

    // Primero obtenemos todos los pokemons de la tabla que queremos agregar
    $query = "SELECT crear_usuario_DGAC();";
    $result = $db -> prepare($query);
    $result -> execute();
    // $pokemons = $result -> fetchAll();




    // Mostramos los cambios en una nueva tabla
    $query = "SELECT * FROM companiasaereas;";
    $result = $db -> prepare($query);
    $result -> execute();
    $companias_aereas = $result -> fetchAll();

    foreach ($companias_aereas as $companias){

        // Luego construimos las querys con nuestro procedimiento almacenado para ir agregando esas tuplas a nuestra bdd objetivo
        // Hacemos una verificacion para ver si el pokemon es legendario porque ese parámetro no se comporta muy bien entre php y sql
        // asi que lo agregamos manualmente al final (por eso los FALSE o TRUE)

        
        $query = "SELECT convertir_compania_aerea('$companias[0]', '$companias[1]');";
    
        // Ejecutamos las querys para efectivamente insertar los datos
        $result = $db -> prepare($query);
        $result -> execute();
        $result -> fetchAll();
    }


    $query = "SELECT * FROM pasaportepasajero;";   //ver bien la tabla
    $result = $db -> prepare($query);
    $result -> execute();
    $pasajeros = $result -> fetchAll();

    foreach ($pasajeros as $pasajero){

        // Luego construimos las querys con nuestro procedimiento almacenado para ir agregando esas tuplas a nuestra bdd objetivo
        // Hacemos una verificacion para ver si el pokemon es legendario porque ese parámetro no se comporta muy bien entre php y sql
        // asi que lo agregamos manualmente al final (por eso los FALSE o TRUE)

        
        $query = "SELECT convertir_pasajeros('$pasajero[0]', '$pasajero[1]');";
    
        // Ejecutamos las querys para efectivamente insertar los datos
        $result = $db -> prepare($query);
        $result -> execute();
        $result -> fetchAll();
    }


?>

<body>

    <h1>Se ha hecho con éxito</h1>
  <form action="../index.php" method="post">
    <input type="submit" value="Volver al inicio">
  </form>
    
<body>

</html>