<?php

    // Nos conectamos a las bdds
    require("../config/conection.php");
    include('../templates/header.html');


    // Enviamos del post la informacion a la query con nuestro procedimiento almacenado que realizará
    // las verificaciones correspondientes
    $codigo = $_POST["codigo"];
    $respuesta = $_POST["respuesta"];
    echo $codigo;
    echo $respuesta;

    $query = "SELECT aceptar_rechazar_vuelo('$codigo', '$respuesta');";    
    // Ejecutamos las querys para efectivamente insertar los datos
    $result = $db -> prepare($query);
    $result -> execute();
    $result -> fetchAll();

    $query2 = "SELECT aceptar_rechazar_vuelo2('$codigo', '$respuesta');";    
    // Ejecutamos las querys para efectivamente insertar los datos
    $result2 = $db2 -> prepare($query2);
    $result2 -> execute();
    $result2 -> fetchAll();

    
?>
<body>
<form action="pagina_admin_dgac.php" method="post">
    <input type="submit" value="Volver">
</form>
<h1>Se ha hecho con éxito</h1>
<body>

</html>