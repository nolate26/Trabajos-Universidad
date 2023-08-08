import React from 'react';
import './paginaprincipal.css';
import LogoutButton from '../profile/Logout'

function PaginaPrincipal() {
  return (
    <div className="container">
      <header className="header">
        <h1 className="title">Risk: San Joaquin</h1>
        <nav className="nav">
          <ul className="nav-list">
            <li className="nav-item">
              <a href='/login'>Iniciar sesión</a>
              <a href='/signup'>Registro</a>
              <LogoutButton></LogoutButton>

            </li>
            <li className="nav-item">
              <a href="/partidas">Jugar!</a>
            </li>
          </ul>
        </nav>
      </header>
      <main className="main">
        <section className="summary">
          <div className="summary-text">
            <h2>RESUMEN</h2>
            <ul>
              <li>El juego se desarrolla en San Joaquin, el cual ha sido separado en cinco sectores de distintos colores y 26 territorios (ver más abajo), pueden participar de 3 a 5 personas.</li>
              <li>Al comienzo de cada partida, cada jugador obtendrá una carta objetivo, la cual contiene la misión secreta del cada uno para poder ganar.</li>
              <li>Durante cada turno, un jugador puede elegir donde atacar y reposicionar sus tropas.</li>
              <li>Un jugador solo puede atacar las casillas que colindan con uno de sus territorios.</li>
              <li>El primero en cumplir su objetivo gana.</li>
            </ul>
          </div>
          <h2>El Tablero de Risk: San Joaquín</h2>
          <div>
            <img src='/assets/img/board.jpg' className='board' alt="Risk San Joaquin" />
          </div>
          <a href="./instructions" className="rules-link">
            Ver reglas
          </a>
        </section>
      </main>
      <a href='/'>Volver Atras</a>
    </div>
  );

}

export default PaginaPrincipal;
