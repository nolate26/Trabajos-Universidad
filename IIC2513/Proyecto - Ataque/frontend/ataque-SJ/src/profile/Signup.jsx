import React, { useState } from 'react';
import axios from 'axios';
import './Login.css';

function Signup() {
    const [name, setName] = useState("");
    const [lastName, setLastName] = useState("");
    const [email, setEmail] = useState("");
    const [birthday, setBirthday] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState(false);
    const [msg, setMsg] = useState("");


    const handleSubmit = async (event) => {
        event.preventDefault();

        axios.post(`${import.meta.env.VITE_BACKEND_URL}/signup`, {
            name: name,
            lastName: lastName,
            email: email,
            image: "", // Establecer un valor predeterminado de cadena vacía
            birthday: birthday,
            password: password
        }).then((response) => {
            console.log('Registro exitoso! Ahora puedes volver y loguearte');
            setError(false);
            setMsg('Registro exitoso! Ahora puedes volver y loguearte');
        }).catch((error) => {
            console.error('Ocurrió un error:', error);
            setError(true); // aquí puede haber más lógica para tratar los errores
        });
    }

    return (
        <div className="Login">
            {msg.length > 0 && <div className="successMsg"> {msg} </div>}

            {error && <div className="error">Hubo un error con el Registro, por favor trata nuevamente.</div>}
            <nav className="nav">
                <ul className="nav-list">
                    <li className="nav-item">
                        <a href='/pagina-principal'>Página principal</a>
                    </li>
                </ul>
            </nav>

            <form onSubmit={handleSubmit}>
                <label>
                    Name:
                    <input
                        type="text"
                        name="name"
                        value={name}
                        onChange={e => setName(e.target.value)}
                        required
                    />
                </label>
                <label>
                    Last Name:
                    <input
                        type="text"
                        name="lastName"
                        value={lastName}
                        onChange={e => setLastName(e.target.value)}
                        required
                    />
                </label>
                <label>
                    Email:
                    <input
                        type="email"
                        name="email"
                        value={email}
                        onChange={e => setEmail(e.target.value)}
                        required
                    />
                </label>
                <label>
                    Birthday:
                    <input
                        type="date"
                        name="birthday"
                        value={birthday}
                        onChange={e => setBirthday(e.target.value)}
                        required
                    />
                </label>
                <label>
                    Password:
                    <input
                        type="password"
                        name="password"
                        value={password}
                        onChange={e => setPassword(e.target.value)}
                        required
                    />
                </label>
                <input type="submit" value="Submit" />
            </form>
        </div>
    );
}

export default Signup;