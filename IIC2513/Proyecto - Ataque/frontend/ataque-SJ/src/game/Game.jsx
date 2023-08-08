import React, { useEffect, useState, useContext } from "react";
import './Game.css';
import ArmyHandler from './ArmyHandler';
import axios from 'axios';
import ThrownDice from './ThrownDice';
import { AuthContext } from '../auth/AuthContext';

function Game() {
  const { id, gameId } = useContext(AuthContext);
  const [playerId, setPlayerId] = useState(0);
  const [update, setUpdate] = useState(true);
  const [gameState, setGameState] = useState('')
  const [attackValues, setAttackValues] = useState(['0','0']);
  const [availableArmies, setAvailableArmies] = useState(0);
  const [defendingArmies, setDefendingArmies] = useState(0);
  const [dice, setDice] = useState([[1,[1]], [1,[1]]]);
  const [showDice, setShowDice] = useState(false);
  const [playMode, setPlayMode] = useState('other');
  const [turn, setTurn] = useState('');
  const [addableArmies, setAddableArmies] = useState(0);
  const [action, setAction] = useState('');
  const [message, setMessage] = useState('');
  const [playerColor, setPlayerColor] = useState('white');
  const [playerObjective, setPlayerObjective] = useState('Conquistar X');

  useEffect(() => {
    axios.get(`${import.meta.env.VITE_BACKEND_URL}/players/player_id/${id}/${gameId}`)
    .then(function (response) {
      setPlayerId(response.data);
      setShowDice(false);
      setAction('Turno terminado')
      setMessage('')
    })
    .catch(function (error) {
      console.log(error);
    });
  }, []);

  useEffect(() => {
    if (playerId != 0) {
      checkTurn();
    }
  }, [playerId]);

  useEffect(() => {
    if (playMode == 'other') {
      setShowDice(false);
      setAction('Turno terminado')
      setMessage('')
    } else if (playMode == 'move') {
      setShowDice(false);
    }
  }, [playMode]);

  function checkTurn() {
    axios.get(`${import.meta.env.VITE_BACKEND_URL}/games/show/${gameId}`)
    .then(function (response) {
      setUpdate(true);
      setTurn(response.data.turn);
      if (response.data.turn == playerId) {
        setPlayMode('add');
        axios.get(`${import.meta.env.VITE_BACKEND_URL}/players/number_armies/${playerId}`)
        .then(function (response) {
          setAddableArmies(response.data);
        }).catch(function (error) {
          console.log(error);
        });
      } else {
        setTimeout(checkTurn, 1000);
      }
    })
    .catch(function (error) {
      console.log(error);
    });
  }

  function handleTurn() {
    let json  = { "gameId": gameId }
    axios.post(`${import.meta.env.VITE_BACKEND_URL}/games/update_turn`, json)
    .then(function (response) {
      console.log(response);
      setTimeout(checkTurn, 1000);
      setUpdate(true);
    }).catch(function (error) {
      console.log(error);
    });
  }

  function handleAttack(clickedValue, armies, color) {
    setShowDice(false);
    console.log(color)
    if (playMode == 'attack') {
      if (attackValues[0] === '0') {
        if (color != playerColor) {
          setMessage('Debes seleccionar un territorio propio')
        } else {
          setAttackValues([clickedValue, '0']);
          setAvailableArmies(armies);
          setMessage('')
        }
      } else if (attackValues[1] === '0') {
        if (color == playerColor) {
          setMessage('Debes seleccionar un territorio enemigo')
        } else {
          setAttackValues([attackValues[0], clickedValue]);
          setDefendingArmies(armies);
          setMessage('')
        }
      } else {
        if (color != playerColor) {
          setMessage('Debes seleccionar un territorio propio')
        } else {
          setAttackValues([clickedValue, '0']);
          setAvailableArmies(armies);
          setMessage('')
        }
      }
    } else if (playMode == 'move') {
      if (attackValues[0] === '0') {
        if (color != playerColor) {
          setMessage('Debes seleccionar un territorio propio')
        } else {
          setAttackValues([clickedValue, '0']);
          setAvailableArmies(armies);
          setMessage('')
        }
      } else if (attackValues[1] === '0') {
        if (color != playerColor) {
          setMessage('Debes seleccionar un territorio propio')
        } else {
          setAttackValues([attackValues[0], clickedValue]);
          setDefendingArmies(armies);
          setMessage('')
        }
      } else {
        if (color != playerColor) {
          setMessage('Debes seleccionar un territorio propio')
        } else {
          setAttackValues([clickedValue, '0']);
          setAvailableArmies(armies);
          setMessage('')
        }
      }
    } else {
      if (attackValues[0] === '0') {
        if (color != playerColor) {
          setMessage('No puedes agregar ejercitos a un territorio que no es tuyo')
        } else {
          setAttackValues([clickedValue, '0']);
          setAvailableArmies(armies);
          setMessage('')
        }
      } else {
        if (color != playerColor) {
          setMessage('No puedes agregar ejercitos a un territorio que no es tuyo')
          setAttackValues(['0', '0']);
        } else {
        setAttackValues([clickedValue, '0']);
        setAvailableArmies(armies);
        setMessage('')
        }
      }
    }
  }

  function randomDice() {
    return Math.floor(Math.random() * 6) + 1;
  }
  function handleAction () {
    if (playMode === 'attack'){
      if (attackValues[0] == '0' | attackValues[1] == '0') {
        console.log('No se puede atacar')
        setShowDice(false);
      } else {
        setShowDice(true);
        let attackers = availableArmies;
        let defenders = defendingArmies;
        if (attackers > 3) {
          attackers = 3;
        }
        if (defenders > 3) {
          defenders = 3;
        }
        let attackDice = [];
        let defenseDice = [];
        for (let i = 0; i < attackers; i++) {
          attackDice.push(randomDice());
        }
        for (let i = 0; i < defenders; i++) {
          defenseDice.push(randomDice());
        }
        let dice = [[attackers, attackDice], [defenders, defenseDice]];
        setDice(dice);
        let json = {  "gameId": gameId,
                  "attacker": attackValues[0],
                  "defender": attackValues[1],
                  "attacker_dice": attackDice,
                  "defender_dice": defenseDice }
        axios.post(`${import.meta.env.VITE_BACKEND_URL}/attack`, json)
        .then(function (response) {
          setUpdate(true);
          setAction(response.data.attackResult)
          setMessage(response.data.consecuences)
        })
        .catch(function (error) {
          console.log(error);
        });
      }
    } else if (playMode === 'add') {
      setShowDice(false);
      if (attackValues[0] == '0') {
        setAction('Debes seleccionar un territorio')
      } else if (addableArmies == 0) {
        setAction('No tienes ejercitos disponibles')
      } else {
        let json = {  "gameId": gameId,
                      "value": attackValues[0],
                      "armies": 1 }
        console.log(json)
        axios.post(`${import.meta.env.VITE_BACKEND_URL}/territories/add`, json)
        .then(function (response) {
          setAction(response.data)
          setMessage('')
          setUpdate(true);
          setAddableArmies(addableArmies - 1);
        }).catch(function (error) {
          console.log(error);
        });
      }
    } else if (playMode === 'move') {
      setShowDice(false);
      if (attackValues[0] == '0' | attackValues[1] == '0') {
        console.log('No se puede mover')
        setShowDice(false);
      } else {
        let attackers = availableArmies;
        if (attackers == 1) {
          setAction('No hay suficientes tropas')
          setMessage('')
          return;
        }
        let json = {  "gameId": gameId,
                  "from": attackValues[0],
                  "to": attackValues[1],
                  "armies": availableArmies - 1 }
        axios.post(`${import.meta.env.VITE_BACKEND_URL}/territories/move`, json)
        .then(function (response) {
          setAction(response.data)
          setMessage('')
          setUpdate(true);
        })
        .catch(function (error) {
          console.log(error);
        });
      }
    }
  }

  useEffect(() => {
    if (update) {
      setUpdate(false);
      axios.get(`${import.meta.env.VITE_BACKEND_URL}/games/show/${parseInt(gameId)}`)
      .then((response) => {
        const data = response.data;
        setGameState(data);
        setAttackValues([0,0])
        setAvailableArmies(0)
        setDefendingArmies(0)
        setTurn(data.turn)
        data.players.forEach((player) => {
          if (player.id == playerId) {
            setPlayerColor(player.color)
          }
        })
      }).catch((error) => {
        console.error('An error trying to update:', error);
      })
    }
  }, [update]);

  return (
    <div style={{heigth:'100vh', overflowY:'scroll', display:'flex'}}>
    <div className="Game" style={{overflowY:'scroll'}}>
      <ArmyHandler gameState={gameState} clicked={handleAttack} />
        <div className="turn">
            <h1>Turno: {turn}</h1>
        </div>
        <div className="infoPanel">
        <p> Tu color: {playerColor}</p>
        <p> Tu objetivo: {playerObjective}</p>
          {playMode == 'add' ? <p> Estado: Agregando Tropas </p> : null}
          {playMode == 'attack' ? <p> Estado: Atacando Territorios </p> : null}
          {playMode == 'move' ? <p> Estado: Moviendo Tropas </p> : null}
          {playMode == 'other' ? <p> Estado: Esperando mi Turno </p> : null}
          {playMode == 'add' ? <button onClick={() => {setPlayMode('attack')}} className="attackButton">Empezar ataque</button> : null}
          {playMode == 'attack' ? <button onClick={() => {setPlayMode('move')}} className="attackButton">Mover Tropas</button> : null}
          {playMode == 'move' ? <button onClick={() => {setPlayMode('other'); handleTurn();}} className="attackButton">Terminar Turno</button> : null}
          <p> Acción Anterior: {action} </p>
          {message != '' ? <p> Consecuencia: {message} </p> : null}
        </div>
        <div className="attackPanel">
          <div className="attackPanelTerritories">
            {playMode == 'add' ? <p> Territorio a agregar: {attackValues[0] == 0 ? 'Seleccionar Territorio' : attackValues[0]} </p> : null}
            {playMode == 'add' ? <p> Ejercitos para agregar: {addableArmies} </p> : null}
            {playMode == 'attack' ? <p> Territorio atacando: {attackValues[0] == 0 ? 'Seleccionar Territorio' : attackValues[0]} </p> : null}
            {playMode == 'attack' ? <p> Ejercitos para atacar: {availableArmies} </p> : null}
            {playMode == 'move' ? <p> Territorio de partida: {attackValues[0] == 0 ? 'Seleccionar Territorio' : attackValues[0]} </p> : null}
            {(playMode == 'move') && (availableArmies == 0) ? <p> Ejercitos a mover: {availableArmies} </p> : null}
            {(playMode == 'move') && (availableArmies != 0) ? <p> Ejercitos a mover: {availableArmies -1} </p> : null}
          </div>
          <div className="attackPanelArmies">
            {playMode == 'attack' ? <p> Territorio defendiendo: {attackValues[1] == 0 ? 'Seleccionar Territorio' : attackValues[1]} </p> : null}
            {playMode == 'attack' ? <p> Ejercitos defendiendo: {defendingArmies} </p> : null}
            {playMode == 'move' ? <p> Territorio de llegada: {attackValues[1] == 0 ? 'Seleccionar Territorio' : attackValues[1]} </p> : null}
            {playMode == 'move' ? <p> Ejercitos en el territorio: {defendingArmies} </p> : null}
          </div>
          <div className="attackPanelButton">
            <button onClick={() => {handleAction()}} className="attackButton">{playMode}</button>
            <div className="attackPanelDice">
              {playMode == 'attack' ? <p>Ataque</p> : null}
              {showDice ? <ThrownDice thrown={dice[0][0]} value={dice[0][1]}/> : null}
              {playMode == 'attack' ? <p>Defensa</p> : null}
              {showDice ? <ThrownDice thrown={dice[1][0]} value={dice[1][1]}/> : null}
            </div>
          </div>
        </div>
      </div>
    </div>
  );

}

export default Game;
