<?php

    // Nos conectamos a las bdds
    require("../config/conection.php");
    include('../templates/header.html');


    // Enviamos del post la informacion a la query con nuestro procedimiento almacenado que realizará
    // las verificaciones correspondientes

    $pasajero1 = $_POST["pasajero1"];
    $pasajero2 = $_POST["pasajero2"];
    $pasajero3 = $_POST["pasajero3"];
    $codigo = $_POST["codigo"];
    $fecha = $_POST["fecha"];
    $comprador = $_POST["comprador"];

    if ($pasajero1 != '' ){
        $pagina = "pagina_generar_reserva.php";}
    if ($pasajero2 != '' ){
        $pagina = "pagina_generar_reserva.php";}
    if ($pasajero3 != '' ){
        $pagina = "pagina_generar_reserva.php";}
    if ($pasajero1 == '' AND $pasajero2 == '' AND $pasajero3 == ''){
        $pagina = "../index.php";
        ?> 

      <h3 align="center" class="tm-color-primary">No ingresaste a ningún pasajero!!!</h3>
      <h3 align="center" class="tm-color-primary">Te vas al inicio!!!</h3>
  <?php }?>


<form action= "<?php echo $pagina ?>" method="get">
    <input type="hidden" name="pasajero1" value="<?php echo $pasajero1?>">
    <input type="hidden" name="pasajero2" value="<?php echo $pasajero2?>">
    <input type="hidden" name="pasajero3" value="<?php echo $pasajero3?>">
    <input type="hidden" name="codigo" value="<?php echo $codigo?>">
    <input type="hidden" name="fecha" value="<?php echo $fecha?>">
    <input type="hidden" name="comprador" value="<?php echo $comprador?>">

    <input align="center" type="submit" value="Siguiente">  
</form>