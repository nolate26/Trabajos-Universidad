<?php

    // Nos conectamos a las bdds
    require("../config/conection.php");
    include('../templates/header.html');

    
    // Mostramos los cambios en una nueva tabla
    $query = "SELECT * FROM codigovuelo WHERE estado = 'pendiente';";
    $result = $db -> prepare($query);
    $result -> execute();
    $vuelos = $result -> fetchAll();

    // Mostramos los cambios en una nueva tabla
    $query2 = "SELECT * FROM tipodevuelo WHERE estado = 'pendiente';";
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
  <h3 align= "center"> Filtrar por fecha</h3>
  <form align="center" action="pagina_filtrar_fecha.php" method="post">
  Respete el formato!!!   
    <br>
    </br>
    Fecha inicio (AAAA-MM-DD):
    <input align="center" type="text" name="fecha1">
    <br>
    </br>
    Fecha termino (AAAA-MM-DD):
    <input align="center" type="text" name="fecha2">
    <input align="center" type="submit" value="Filtrar">
  </form>

  <br></br>


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


<form action="../index.php" method="post">
    <input type="submit" value="Volver al inicio">
</form>

<body>

</html>