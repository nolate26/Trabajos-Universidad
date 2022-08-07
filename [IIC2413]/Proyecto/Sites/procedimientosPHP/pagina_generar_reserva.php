<?php

    // Nos conectamos a las bdds
    require("../config/conection.php");
    include('../templates/header.html');

    $pasajero1 = $_GET["pasajero1"];
    $pasajero2 = $_GET["pasajero2"];
    $pasajero3 = $_GET["pasajero3"];
    $codigo = $_GET["codigo"];
    $fecha = $_GET["fecha"];
    $comprador = $_GET["comprador"];

    $verificacion1 = FALSE;
    $verificacion2 = FALSE;
    $verificacion3 = FALSE;
    $verificacion4 = FALSE;

    // VERIFICAR EXISTE EL PASAPORTE 
    $query_pasajero = "SELECT pasaporte_pasajero from pasajeros;";
    $result1 = $db -> prepare($query_pasajero);
    $result1 -> execute();
    $resultado = $result1 -> fetchAll();

    foreach($resultado as $usuario){
      if ($usuario[0] ==  $pasajero1){
        $verificacion1 = TRUE;
    } if ($usuario[0] ==  $pasajero2){
      $verificacion2 = TRUE;
    } if ($usuario[0] ==  $pasajero3){
        $verificacion3 = TRUE;
    } if ($usuario[0] ==  $comprador){
      $verificacion4 = TRUE;
    }}

    if ($pasajero1 == '' AND $verificacion1 == FALSE){
      $verificacion1 = TRUE;}
    if ($pasajero2 == '' AND $verificacion2 == FALSE){
      $verificacion2 = TRUE;}
    if ($pasajero3 == '' AND $verificacion3 == FALSE){
      $verificacion3 = TRUE;}


    if ($verificacion1 == FALSE OR $verificacion2 == FALSE OR $verificacion3 == FALSE OR $verificacion4 == FALSE){
      ?> 

      <h3 align="center" class="tm-color-primary">INGRESASTE UN PASAPORTE QUE NO EXISTE!!!</h3>
      <h3 align="center" class="tm-color-primary">VUELVE AL INICIO!</h3>
  <?php }?>
  <?php

    if ($verificacion1 == TRUE AND $verificacion2 == TRUE AND $verificacion3 == TRUE ){
      $query_fecha = "SELECT pasajeros.pasaporte_pasajero, codigovuelo.fecha_salida, codigovuelo.fecha_llegada from pasajeros, ticketreserva, idvuelo, codigovuelo where pasajeros.numero_ticket = ticketreserva.numero_ticket and ticketreserva.vuelo_id = idvuelo.vuelo_id and idvuelo.codigo_vuelo = codigovuelo.codigo_vuelo;";
      $result = $db -> prepare($query_fecha);
      $result -> execute();
      $resultado1 = $result -> fetchAll();
      foreach($resultado1 as $usuario){
        $f1 = date('Y-m-d', strtotime($usuario[1]));
        $f2 = date('Y-m-d', strtotime($usuario[2]));
        $f_oficial = date('Y-m-d', strtotime($fecha));

        if ($usuario[0] ==  $pasajero1 AND ($f_oficial >= $f1) AND ($f_oficial <= $f2) ){
          $verificacion1 = FALSE;
      } if ($usuario[0] ==  $pasajero2 AND ($f_oficial >= $f1) AND ($f_oficial <= $f2) ){
        $verificacion2 = FALSE;
      } if ($usuario[0] ==  $pasajero2 AND ($f_oficial >= $f1) AND ($f_oficial <= $f2)){
        $verificacion3 = FALSE;
      }}

      if ($verificacion1 == FALSE OR $verificacion2 == FALSE OR $verificacion3 == FALSE ){
        ?> 
      <h3 align="center" class="tm-color-primary">UN PASAPORTE TIENE UN TOPE HORARIO CON OTRO VUELO EXISTENTE!!!</h3>
      <h3 align="center" class="tm-color-primary">VUELVE AL INICIO!</h3>
  <?php }}?>
    
  <?php
    

    if ($verificacion1 == TRUE AND $verificacion2 == TRUE AND $verificacion3 == TRUE ){
      $query = "SELECT generar_reserva('$pasajero1', '$pasajero2', '$pasajero3', '$codigo', '$comprador');";
      $result = $db -> prepare($query);
      $result -> execute();
      ?> 
      <h3 align="center" class="tm-color-primary">Se agregó la reserva</h3>
  <?php }?>
<body>

  <form action="../index.php" method="post">
    <input type="submit" value="Volver al inicio">
  </form>

<body>

</html>