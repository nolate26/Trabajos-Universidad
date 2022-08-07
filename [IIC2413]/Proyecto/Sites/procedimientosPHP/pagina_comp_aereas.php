<?php

    // Nos conectamos a las bdds
    require("../config/conection.php");
    include('../templates/header.html');

    $usuario1 = $_GET["usuario"];
    //query para nombre compania
    $query0 = "SELECT nombre_compania FROM companiasaereas WHERE '$usuario1' = codigo_compania";
    $result0 = $db -> prepare($query0);
    $result0 -> execute();
    $nombre_aerolinea = $result0 -> fetchAll();
    // query aceptados
    $query1 = "SELECT codigovuelo.codigo_vuelo, codigovuelo.fecha_salida, codigovuelo.fecha_llegada FROM codigovuelo, (SELECT codigo_vuelo FROM codigovuelocompania WHERE codigo_compania = '$usuario1') as vuelos WHERE codigovuelo.codigo_vuelo = vuelos.codigo_vuelo AND codigovuelo.estado = 'aceptado';";
    $result1 = $db -> prepare($query1);
    $result1 -> execute();
    $vuelos_aceptados1 = $result1 -> fetchAll();
    //query rechazados
    $query2 = "SELECT codigovuelo.codigo_vuelo, codigovuelo.fecha_salida, codigovuelo.fecha_llegada FROM codigovuelo, (SELECT codigo_vuelo FROM codigovuelocompania WHERE codigo_compania = '$usuario1') as vuelos WHERE codigovuelo.codigo_vuelo = vuelos.codigo_vuelo AND codigovuelo.estado = 'rechazado';";
    $result2 = $db -> prepare($query2);
    $result2 -> execute();
    $vuelos_rechazados2 = $result2 -> fetchAll();

    $query3 = "SELECT distinct  codigo, fecha_salida, fecha_llegada from tipodevuelo, propuestavuelo, companiaaerea where tipodevuelo.id = propuestavuelo.id and  companiaaerea.codigo_compania = propuestavuelo.codigo_compania and propuestavuelo.codigo_compania = '$usuario1' and tipodevuelo.estado = 'aceptado';";
    $result3 = $db2 -> prepare($query3);
    $result3 -> execute();
    $vuelos_aceptados3 = $result3 -> fetchAll();
    
    $query4 = "SELECT distinct  codigo, fecha_salida, fecha_llegada from tipodevuelo, propuestavuelo, companiaaerea where tipodevuelo.id = propuestavuelo.id and  companiaaerea.codigo_compania = propuestavuelo.codigo_compania and propuestavuelo.codigo_compania = '$usuario1' and tipodevuelo.estado = 'rechazado';";
    $result4 = $db2 -> prepare($query4);
    $result4 -> execute();
    $vuelos_rechazados4 = $result4 -> fetchAll();


?>
    <h3> Nombre Compania <h3>
    <table>
    <tr>
    <th>Nombre compania</th>
    </tr>
    <?php
    foreach ($nombre_aerolinea as $aerolinea) {
    echo "<tr><td>$aerolinea[0]</td></tr>";
    }

    ?>
    </table>
<?php
    
?>
    <h3> Vuelos Aceptados <h3>
            <table>
    <tr>
      <th>Codigo Vuelo</th>
      <th>Fecha salida</th>
      <th>Fecha llegada</th>
    </tr>
  <?php
	foreach ($vuelos_aceptados1 as $vuelo1) {
  		echo "<tr><td>$vuelo1[0]</td><td>$vuelo1[1]</td><td>$vuelo1[2]</td></tr>";
	}
    foreach ($vuelos_aceptados3 as $vuelo3) {
        echo "<tr><td>$vuelo1[0]</td><td>$vuelo1[1]</td><td>$vuelo1[2]</td></tr>";
  }

  ?>
	    </table>
<?php
    
?>
    <h3> Vuelos Rechazados <h3>
        <table>
    <tr>
      <th>Codigo Vuelo</th>
      <th>Fecha salida</th>
      <th>Fecha llegada</th>
    </tr>
    <?php
    foreach ($vuelos_rechazados2 as $vuelo3) {
        echo "<tr><td>$vuelo3[0]</td><td>$vuelo3[1]</td><td>$vuelo3[2]</td></tr>";
    }
    foreach ($vuelos_rechazados4 as $vuelo4) {
        echo "<tr><td>$vuelo4[0]</td><td>$vuelo4[1]</td><td>$vuelo4[2]</td></tr>";
    }

    ?>
    </table>
<body>

<form action="../index.php" method="post">
    <input type="submit" value="Volver al inicio">
</form>

<body>
</html>