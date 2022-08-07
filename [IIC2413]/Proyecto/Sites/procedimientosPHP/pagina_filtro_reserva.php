<?php

    // Nos conectamos a las bdds
    require("../config/conection.php");
    include('../templates/header.html');


    // Enviamos del post la informacion a la query con nuestro procedimiento almacenado que realizará
    // las verificaciones correspondientes
    $ciudad_salida = $_POST["origen"];
    $ciudad_llegada = $_POST["llegada"];
    $fecha_salida = $_POST["fecha_despegue"];
    $t1 = ' 00:00:00';
    $t2 = ' 23:59:00';
    $fecha_salida1 = $fecha_salida . $t1;
    $fecha_salida2 = $fecha_salida . $t2;

    // Mostramos los cambios en una nueva tabla
    $query1 = "SELECT * FROM (SELECT a.ciudad_origen, idaerodromos.nombre_ciudad AS ciudad_llegada, codigovuelo.codigo_vuelo, codigovuelo.estado, codigovuelo.fecha_salida, codigovuelo.fecha_llegada FROM 
    (SELECT idaerodromos.nombre_ciudad AS ciudad_origen, codigovuelo.codigo_vuelo, codigovuelo.fecha_salida, codigovuelo.fecha_llegada FROM codigovuelo, idaerodromos WHERE codigovuelo.aerodromo_salida_id = idaerodromos.aerodromo_id AND estado = 'aceptado') AS a, codigovuelo, idaerodromos 
    WHERE codigovuelo.aerodromo_llegada_id = idaerodromos.aerodromo_id AND estado = 'aceptado' AND codigovuelo.codigo_vuelo = a.codigo_vuelo) AS tabla WHERE tabla.ciudad_origen = '$ciudad_salida' AND tabla.ciudad_llegada = '$ciudad_llegada' AND tabla.fecha_salida BETWEEN '$fecha_salida1' and '$fecha_salida2';";
    $result1 = $db -> prepare($query1);
    $result1 -> execute();
    $vuelos1 = $result1 -> fetchAll();

    $query2 = "SELECT * FROM (SELECT distinct a.ciudad_origen, aerodromos.nombre_ciudad as ciudad_llegada, tipodevuelo.codigo, tipodevuelo.estado, tipodevuelo.fecha_salida, tipodevuelo.fecha_llegada from (select aerodromos.nombre_ciudad as ciudad_origen, tipodevuelo.codigo, tipodevuelo.fecha_salida, tipodevuelo.fecha_llegada from tipodevuelo, aerodromos where tipodevuelo.aerodromo_salida_id = aerodromos.aerodromo_id and estado = 'aceptado') as a, tipodevuelo, aerodromos where tipodevuelo.aerodromo_llegada_id = aerodromos.aerodromo_id and estado = 'aceptado' and tipodevuelo.codigo = a.codigo) AS tabla WHERE tabla.ciudad_origen = '$ciudad_salida' AND tabla.ciudad_llegada = '$ciudad_llegada' AND tabla.fecha_salida = '$fecha_salida';";
    $result2 = $db2 -> prepare($query2);
    $result2 -> execute();
    $vuelos2 = $result2 -> fetchAll();
?>

    <table>
    <tr>
        <th>Ciudad de origen</th>
        <th>Ciudad de llegada</th>
        <th>Codigo Vuelo</th>
        <th>Estado</th>
        <th>Fecha salida</th>
        <th>Fecha llegada</th>
    </tr>
    <?php
    foreach ($vuelos1 as $vuelo) {
        echo "<tr><td>$vuelo[0]</td><td>$vuelo[1]</td><td>$vuelo[2]</td><td>$vuelo[3]</td><td>$vuelo[4]</td><td>$vuelo[5]</td></tr>";
        
    }
    foreach ($vuelos2 as $vuelo2) {
        echo "<tr><td>$vuelo2[0]</td><td>$vuelo2[1]</td><td>$vuelo2[2]</td><td>$vuelo2[3]</td><td>$vuelo2[4]</td><td>$vuelo2[5]</td></tr>";
    }
    ?>

    </table>
<body>
    <h3 align= "center">Genere una reserva</h3>
  <form align="center" action="revisar_pasajeros.php" method="post">
    Pasajero 1 (RUT):
    <input align="center" type="text" name="pasajero1">
    <br/>
    <br/>
    Pasajero 2 (RUT):
    <input align="center" type="text" name="pasajero2">
    <br/>
    <br/>
    Pasajero 3 (RUT):
    <input align="center" type="text" name="pasajero3">
    <br/>
    <br/>
    Código de vuelo a elegir:
    <input align="center" type="text" name="codigo">
    <br/>
    <br/>
    Fecha (AAAA-MM-DD HH:MM:SS):
    <input align="center" type="text" name="fecha">
    <br/>
    <br/>
    RUT del comprador:
    <input align="center" type="text" name="comprador">
    <br/>
    <br/>
    <input align="center" type="submit" value="Generar Reserva">
  </form>


<body>

</html>