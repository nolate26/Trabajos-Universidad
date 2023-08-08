import './CreateGame.css'
import React, { useState } from 'react';
import axios from 'axios';

export default function CreateGame() {
    const [msg, setMsg] = useState("");
    const [error, setError] = useState(false);
    const [mail1, setMail1] = useState("");
    const [mail2, setMail2] = useState("");
    const [mail3, setMail3] = useState("");
    const [mail4, setMail4] = useState("");

    const handleSubmit = async (event) => {
        event.preventDefault();

        axios.post(`${import.meta.env.VITE_BACKEND_URL}/games/create`, {
            mails: [mail1, mail2, mail3, mail4]
        }).then((response) => {
            console.log('Partida creada con exito! Ahora puedes acceder a tu partida');
            setError(false);
            setMsg('Partida creada con exito! Ahora puedes volver y acceder a tu partida');
        }).catch((error) => {
            console.error('Ocurrió un error:', error);
            setError(true); // aquí puede haber más lógica para tratar los errores
        });
    }

    return (
        <div className="Login">
            {msg.length > 0 && <div className="successMsg"> {msg} </div>}

            {error && <div className="error">Hubo un error al crear partida, revisa los datos e intenta nuevamente.</div>}
            <nav className="nav">
                <ul className="nav-list">
                    <li className="nav-item">
                        <a href='/pagina-principal'>Página principal</a>
                    </li>
                </ul>
            </nav>

            <form onSubmit={handleSubmit}>
                <label>
                    Your Email:
                    <input
                        type="text"
                        name="mail1"
                        value={mail1}
                        onChange={e => setMail1(e.target.value)}
                        required
                    />
                </label>
                <label>
                    Mail second player:
                    <input
                        type="text"
                        name="mail2"
                        value={mail2}
                        onChange={e => setMail2(e.target.value)}
                        required
                    />
                </label>
                <label>
                    Mail third player:
                    <input
                        type="text"
                        name="mail3"
                        value={mail3}
                        onChange={e => setMail3(e.target.value)}
                        required
                    />
                </label>
                <label>
                    Mail fourth player:
                    <input
                        type="text"
                        name="mail4"
                        value={mail4}
                        onChange={e => setMail4(e.target.value)}
                        required
                    />
                </label>
                <input type="submit" value="Submit" />
            </form>
        </div>
    );
}
