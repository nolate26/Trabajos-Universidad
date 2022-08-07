<?php include('templates/header.html');   ?>

<body>
    <header class="tm-site-header">
        <h1 class="tm-mt-0 tm-mb-15"><span class="tm-color-primary">Plataforma de gestión operativa de vuelos:</span></h1>
        <h1 class="tm-mt-0 tm-mb-15"><span class="tm-color-primary">Grupo 54-111</span></h1>
        <em class="tm-tagline tm-color-light-gray">Aquí podrás encontrar información sobre los vuelos</em>
    </header>

    <!-- Video banner 400 px height -->
    <div id="tm-video-container">
        <video autoplay muted loop id="tm-video">
            <source src="video/video.mp4" type="video/mp4">
        </video>  
        <i id="tm-video-control-button" class="fas fa-pause"></i>
    </div>
    <div class="tm-container">

        <h3 align="center" class="tm-color-primary">Pulse para importar usuarios</h3>
        <form align="center" action="procedimientosPHP/procedimiento_importar_usuario.php" method="post">
          <input align="center" type="submit" value="Importar Usuarios">
        </form>     
        <br></br>
        <h3 align="center" class="tm-color-primary">Login</h3>
        <form align="center" action="procedimientosPHP/procedimiento_login.php" method="post">
          Usuario:
          <input align="center" type="text" name="Usuario">
          <br/>
          <br/>
          Contraseña:
          <input align="center" type="password" name="Contrasena">
          <br/>
          <br/><br/>
          <input align="center" type="submit" value="Ingresar">
        </form>
    </div>
  <br>
  <footer class="tm-footer">
    <span>Copyright &copy; 2022 Nolate26</span>
    <span>Web Designed by Nolate26
</footer>

</body>
</html>
