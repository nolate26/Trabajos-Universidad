import React, { useState, useEffect, useContext } from 'react';
import './Partidas.css';
import axios from 'axios';
import { AuthContext } from '../auth/AuthContext';
import { useNavigate } from 'react-router-dom';
import UserCheck from '../protected/UserCheck';

function Partidas() {
  const { token } = useContext(AuthContext)
  const navigate = useNavigate();
  const [games, setGames] = useState([]);
  const { id, setGameId } = useContext(AuthContext);
  
  useEffect(() => {
    axios.get(`${import.meta.env.VITE_BACKEND_URL}/players/user_games/${id}`)
    .then(function (response) {
      setGames(response.data);
      console.log(response.data);
    })
    .catch(function (error) {
      console.log(error);
    });
  }, []);
  
  useEffect(() => {
    console.log(token);
    axios({
      method: 'get',
      url: `${import.meta.env.VITE_BACKEND_URL}/scope-example/protecteduser`,
      headers: {
        'Authorization': `Bearer ${token}`
      }
    })
      .then(response => {
        console.log(response.data.user)
      })
      .catch(error => {
        navigate('/pagina-principal');
      });
  }, [token, navigate]);
  
  return (
    <div className="container">
      <header className="header">
        <h1 className="title">Risk: San Joaquin</h1>
        <nav className="nav">
          <ul className="nav-list">
            <li className="nav-item">
              <a href="/pagina-principal">Atras</a>
            </li>
            <li className="nav-item">
              <a href="/create-game">Crear partida</a>
            </li>
          </ul>
        </nav>
      </header>
      <main className="main">
        <section className="summary">
          <div className="summary-text">
            <h2>Partidas en curso</h2>
              {games.map((game) => (
                <div className="game">
                  <h3>Partida {game}</h3>
                  <p>Estado: por implementar</p>
                  <p>Jugadores: 4</p>
                  <a href="/game">
                    <button className='Partida' onClick={() => {setGameId(game)}}>Entrar a Partida</button>
                  </a>
                </div>
              ))}
          </div>
        </section>
      </main>
      <UserCheck />
    </div>
  );

}

export default Partidas;
