<?php

    // Nos conectamos a las bdds
    require("../config/conection.php");
    include('../templates/header.html');


    // Enviamos del post la informacion a la query con nuestro procedimiento almacenado que realizará
    // las verificaciones correspondientes
    $fecha1 = $_POST["fecha1"];
    $fecha2 = $_POST["fecha2"];
    echo $fecha1;
    echo $fecha2;

 // operaciondespegue.fecha_despegue between '$oficial1' and '$oficial2'

    // Mostramos los cambios en una nueva tabla
    $query = "SELECT * FROM codigovuelo WHERE estado = 'pendiente' AND ((fecha_salida BETWEEN '$fecha1' and '$fecha2') OR (fecha_llegada BETWEEN '$fecha1' and '$fecha2') OR (fecha_salida < '$fecha1' AND fecha_llegada > '$fecha2'));";
    $result = $db -> prepare($query);
    $result -> execute();
    $vuelos = $result -> fetchAll();


    $query2 = "SELECT * FROM tipodevuelo WHERE estado = 'pendiente' AND ((fecha_salida BETWEEN '$fecha1' and '$fecha2') OR (fecha_llegada BETWEEN '$fecha1' and '$fecha2') OR (fecha_salida < '$fecha1' AND fecha_llegada > '$fecha2'));";
    $result2 = $db2 -> prepare($query2);
    $result2 -> execute();
    $vuelos2 = $result2 -> fetchAll();
?>
    <table>
    <tr>
        <th>Aerodromo Salida ID</th>
        <th>Codigo Vuelo</th>
        <th>Estado</th>
        <th>Fecha salida</th>
        <th>Fecha llegada</th>
    </tr>
    <?php
    foreach ($vuelos as $vuelo) {
        echo "<tr><td>$vuelo[0]</td><td>$vuelo[3]</td><td>$vuelo[9]</td><td>$vuelo[5]</td><td>$vuelo[6]</td></tr>";
        
    }
    foreach ($vuelos2 as $vuelo2) {
        echo "<tr><td>$vuelo2[5]</td><td>$vuelo2[2]</td><td>$vuelo2[1]</td><td>$vuelo2[3]</td><td>$vuelo2[4]</td></tr>";
    }
    ?>

    </table>
<body>

<h3 align= "center">Aceptar y rechazar propuestas de vuelo</h3>
  <form align="center" action="pagina_aceptar_rechazar.php" method="post">
    Código de vuelo:
    <input align="center" type="text" name="codigo">
    <br/>
    <br/>
    <select name="respuesta">
      <option value="aceptar">Aceptar</option>
      <option value="rechazar">Rechazar</option>
    </select> 
    <input align="center" type="submit" value="Ingresar">
  </form>


<form action="pagina_admin_dgac.php" method="post">
    <input type="submit" value="Volver">
</form>
<h1>Se ha hecho con éxito</h1>
<body>

</html>