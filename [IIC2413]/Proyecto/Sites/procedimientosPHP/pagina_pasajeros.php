<?php

    // Nos conectamos a las bdds
    require("../config/conection.php");
    include('../templates/header.html');
    $usuario1 = $_GET["usuario"];


    $query = "SELECT nombre_pasajero FROM pasaportepasajero WHERE pasaporte_pasajero = '$usuario1';";
    $result = $db -> prepare($query);
    $result -> execute();
    $nombre = $result -> fetchAll();

    $query1 = "SELECT DISTINCT  reservas.reserva_id, reservas.codigo_reserva, reservas.vuelo_id FROM pasajerocomprador, reservas WHERE pasaporte = '$usuario1';";
    $result1 = $db -> prepare($query1);
    $result1 -> execute();
    $reservas = $result1 -> fetchAll();

    // "SELECT DISTINCT nombre_ciudad FROM tipodevuelo, aerodromos WHERE tipodevuelo.aerodromo_llegada_id = aerodromos.aerodromo_id AND tipodevuelo.estado = 'aceptado';"
    // "SELECT DISTINCT nombre_ciudad FROM Tipo_de_vuelo, aerodromos WHERE Tipo_de_vuelo.aerodromo_llegada_id = aerodromo.aerodromo_id AND Tipo_de_vuelo.estado = 'aceptado';"


    
?>
<table>
    <tr>
        <th>Nombre Pasajero</th>
        <th>Pasaporte</th>
    </tr>
    <?php
    foreach ($nombre as $n) {
        echo "<tr><td>$n[0]</td><td>$usuario1</td></tr>";
    }
    ?>

</table>

<table>
    <tr>
        <th>Reserva Id</th>
        <th>Código Reserva</th>
        <th>Vuelo Id</th>
    </tr>
    <?php
    foreach ($reservas as $reserva) {
        echo "<tr><td>$reserva[0]</td><td>$reserva[1]</td><td>$reserva[2]</td></tr>";
    }
    ?>

</table>

<body>
<h3 align= "center">Filtro de vuelos</h3>
  <form align="center" action="pagina_filtro_reserva.php" method="post">
    Ciudad origen
    <select name="origen">
      <option value="Atenas">Atenas</option>
      <option value="El Cairo">El Cairo</option>
      <option value="Paris">Paris</option>
      <option value="Beijing">Beijing</option>
      <option value="Lima">Lima</option>
      <option value="Ciudad del Cabo">Ciudad del Cabo</option>
      <option value="Tokio">Tokio</option>
      <option value="Nueva Delhi">Nueva Delhi</option>
      <option value="San Francisco">San Francisco</option>
      <option value="Caracas">Caracas</option>
      <option value="Milan">Milan</option>
      <option value="Chicago">Chicago</option>
      <option value="Londres">Londres</option>
      <option value="Sao Pablo">Sao Pablo</option>
      <option value="Ibiza">Ibiza</option>
      <option value="Cancun">Cancun</option>
      <option value="Tel Aviv">Tel Aviv</option>
      <option value="Estambul">Estambul</option>
      <option value="Seul">Seul</option>
      <option value="Amsterdam">Amsterdam</option>
      <option value="Sidney">Sidney</option>
      <option value="Madrid">Madrid</option>
      <option value="Barcelona">Barcelona</option>
      <option value="Nueva York">Nueva York</option>
      <option value="Shangai">Shangai</option>
      <option value="Montevideo">Montevideo</option>
      <option value="Toronto">Toronto</option>
      <option value="Santiago">Santiago</option>
      <option value="La Paz">La Paz</option>
      <option value="Buenos Aires">Buenos Aires</option>
      <option value="Roma">Roma</option>
      <option value="Hong Kong">Hong Kong</option>
      <option value="Rio de Janeiro">Rio de Janeiro</option>
      <option value="Melbourne">Melbourne</option>
      <option value="Miami">Miami</option>
    </select> 
    Ciudad llegada
    <select name="llegada">
      <option value="Atenas">Atenas</option>
      <option value="El Cairo">El Cairo</option>
      <option value="Paris">Paris</option>
      <option value="Beijing">Beijing</option>
      <option value="Lima">Lima</option>
      <option value="Ciudad del Cabo">Ciudad del Cabo</option>
      <option value="Tokio">Tokio</option>
      <option value="Nueva Delhi">Nueva Delhi</option>
      <option value="San Francisco">San Francisco</option>
      <option value="Caracas">Caracas</option>
      <option value="Milan">Milan</option>
      <option value="Chicago">Chicago</option>
      <option value="Londres">Londres</option>
      <option value="Sao Pablo">Sao Pablo</option>
      <option value="Ibiza">Ibiza</option>
      <option value="Cancun">Cancun</option>
      <option value="Tel Aviv">Tel Aviv</option>
      <option value="Estambul">Estambul</option>
      <option value="Seul">Seul</option>
      <option value="Amsterdam">Amsterdam</option>
      <option value="Sidney">Sidney</option>
      <option value="Madrid">Madrid</option>
      <option value="Barcelona">Barcelona</option>
      <option value="Nueva York">Nueva York</option>
      <option value="Shangai">Shangai</option>
      <option value="Montevideo">Montevideo</option>
      <option value="Toronto">Toronto</option>
      <option value="Santiago">Santiago</option>
      <option value="La Paz">La Paz</option>
      <option value="Buenos Aires">Buenos Aires</option>
      <option value="Roma">Roma</option>
      <option value="Hong Kong">Hong Kong</option>
      <option value="Rio de Janeiro">Rio de Janeiro</option>
      <option value="Melbourne">Melbourne</option>
      <option value="Miami">Miami</option>
    </select> 
    <br>
    </br>
    Fecha de despegue (AAAA-MM-DD):
    <input align="center" type="text" name="fecha_despegue">
    <br/>
    <br/>
    <input align="center" type="submit" value="Ingresar">
  </form>
    <form action="../index.php" method="post">
        <input type="submit" value="Volver al inicio">
    </form>


    <body>

    </html>