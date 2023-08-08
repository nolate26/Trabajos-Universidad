import React, { useState } from 'react';
import './Example.css';
import ThrowDice from './ThrownDice.jsx';

export default function Example(props){
    const [dado_ataque, setDado_ataque] = useState([1]);
    const [dado_defensa, setDado_defena] = useState([1]);
    const [resultado, setResultado] = useState('GANA DEFENSOR');

    function calcular_resutlado(ataque, defensa){
        if (ataque > defensa){
            return 'GANA ATACANTE'
        } else if (ataque <= defensa){
            return 'GANA DEFENSOR'
        };
    };

    return (
        <>
        <h2 className='jugador'> ATACANTE:</h2>
            <div className='dicethrow'>
                <ThrowDice thrown={1} value={dado_ataque}/>
            </div>
            <button
            type="button"
            onClick={() => setDado_ataque([Math.floor(Math.random() * 6) + 1])}
            >Lanzar Dado</button>

        <h2 className='jugador'> DEFENSA:</h2>
            <div className='dicethrow'>
                <ThrowDice thrown={1} value={dado_defensa}/>
            </div>
            <button
            type="button"
            onClick={() => setDado_defena([Math.floor(Math.random() * 6) + 1])}
            >Lanzar Dado</button>
        <h2 className='jugador'> RESULTADO: {resultado}</h2>
        <button
            type="button"
            onClick={() => setResultado(calcular_resutlado(dado_ataque[0], dado_defensa[0]))}
        >Simular</button>
      </>
    );
  }


// var dado_ataque = Math.floor(Math.random() * 6) + 1;
// var dado_defensa = Math.floor(Math.random() * 6) + 1;
