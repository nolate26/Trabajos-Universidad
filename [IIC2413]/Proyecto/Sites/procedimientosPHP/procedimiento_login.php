<?php

    // Nos conectamos a las bdds
    require("../config/conection.php");
    include('../templates/header.html');


    // Enviamos del post la informacion a la query con nuestro procedimiento almacenado que realizará
    $login = FALSE;
    // las verificaciones correspondientes
    $usuario1 = $_POST["Usuario"];
    $contrasena1 = $_POST["Contrasena"];
    $query = "SELECT *, COUNT(*) as cuenta FROM usuarios WHERE username LIKE '$usuario1' AND contrasena LIKE '$contrasena1' GROUP BY id_usuario;";
    $result = $db -> prepare($query);
    $result -> execute();


    // Si nos interesa acceder a los booleanos que retorna el procedimiento, debemos hacer fetch de los resultados
    $resultado = $result -> fetchAll();

    foreach($resultado as $usuario){
      if ($usuario['cuenta'] == 1 AND $usuario['tipo'] == 'Admin DGAC'){
        $pagina = "pagina_admin_dgac.php";
        $login = TRUE;
         //nos vamos a pag de admin dgac
    } if ($usuario['cuenta'] == 1 AND $usuario['tipo'] == 'Compañía Aérea'){
        $pagina = "pagina_comp_aereas.php"; //nos vamos a la página de C.aéreas
        $login = TRUE;
    } if ($usuario['cuenta'] == 1 AND $usuario['tipo'] == 'Pasajero'){
        $pagina = "pagina_pasajeros.php";  //nos vamos a la página de Pasajeros
        $login = TRUE;
    }}

    if ($login == TRUE){
      ?> 
      <h3 align="center" class="tm-color-primary">Login realizado con éxito</h3>
  <?php }?>


  <?php 
    if ($login == FALSE){
      $pagina = "../index.php";?> 
      <h2 align="center" class="tm-tagline tm-color-light-gray">Nombre de usuario o contraseña inválida</h2>

      <h3 align="center" class="tm-tagline tm-color-light-gray">Vuelva a la página principal</h3>
    <?php }?>

<body>
    <form action= "<?php echo $pagina ?>" method="get">
      <input type="hidden" name="usuario" value="<?php echo $usuario1?>">
      <input align="center" type="submit" value="Dirigirse a la página">  
    </form>
<body>
</html>