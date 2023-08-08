import React, { useState } from 'react';
import './ExampleMove.css';

export default function ExampleMove() {
    const [choose_selected, setChoose_selected] = useState(true);
    const [choose_not_selected, setChoose_not_selected] = useState(false);
    const [choose_enemy, setChoose_enemy] = useState(false);
    const [choose_blank, setChoose_block] = useState(false);

    function clickSelected() {
        setChoose_selected(true);
        setChoose_not_selected(false);
        setChoose_enemy(false);
        setChoose_block(false);
    }
    function clickNotSelected() {
        setChoose_selected(false);
        setChoose_not_selected(true);
        setChoose_enemy(false);
        setChoose_block(false);
    }
    function clickEnemy() {
        setChoose_selected(false);
        setChoose_not_selected(false);
        setChoose_enemy(true);
        setChoose_block(false);
    }
    function clickBlank() {
        setChoose_selected(false);
        setChoose_not_selected(false);
        setChoose_enemy(false);
        setChoose_block(true);
    }

    function validarMovimiento() {
        if (choose_selected) {
            return 'Ya estas en este bloque.';
        } else if (choose_not_selected) {
            return 'Puedes mover tus tropas a este bloque.';
        } else if (choose_enemy) {
            return 'No puedes mover tus tropas a este bloque, hay un enemigo.';
        } else if (choose_blank) {
            return 'No esta permitido mover tus tropas a este bloque.';
        }
    }


    return (
        <>
            <h3>En este mapa super simplificado, tus tropas se encuentran en el primer bloque azul. El bloque a la derecha, también azul, te pertenece
                y puedes mover tus tropas a este bloque. El bloque rojo es un enemigo y no te pertenece, por lo que no puedes mover tus tropas a este bloque.
                Finalmente, el bloque blanco es un terreno "fuera de juego". Prueba presionando los bloques para ver que pasa!
            </h3>
            <div className="container2">
                <div className="block selected"
                    style={{ borderStyle: choose_selected ? 'outset' : 'solid' }}
                    onClick={clickSelected}>
                    <div>
                        <img src='/assets/img/soldiers/student1.png' alt="Student" className="student" />
                    </div>
                </div>
                <div className="block not-selected"
                    style={{ borderStyle: choose_not_selected ? 'outset' : 'solid' }}
                    onClick={clickNotSelected}> </div>
                <div className="block enemy"
                    style={{ borderStyle: choose_enemy ? 'outset' : 'solid' }}
                    onClick={clickEnemy}> </div>
                <div className="block blank"
                    style={{ borderStyle: choose_blank ? 'outset' : 'solid' }}
                    onClick={clickBlank}> </div>
            </div>
            <h3 className='jugador'>{validarMovimiento()}</h3>
        </>
    );
}
