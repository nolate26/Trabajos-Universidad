import { useState, useContext } from "react";
import './UserWelcome.css'
import imagenNicolas from '/assets/img/nicolas.png'
import imagenBorja from '/assets/img/borja.jpeg'

export default function UserWelcome() {

    const [nombre, setNombre] = useState(null)

    function handleChange(nombre) {
        setNombre(nombre);
    }

    return (
        <>
            <div>
                <h1> El Equipo OLMA</h1>
                <div className="integrante">
                    <img src={imagenNicolas} alt="Avatar de Integrante 1" />
                    <h2>Nicolás Olate</h2>
                    <p>Estudiante de Ingeniería Civil y Major Computación. Es uno de mis juegos favoritos el "Ataque", pero nose si será mejor que Risk: San Joaquín.</p>
                </div>
                <div className="integrante">
                    <img src={imagenBorja} alt="Avatar de Integrante 2" />
                    <h2>Borja Márquez de la Plata</h2>
                    <p>
                        Estudiante de Ingeniería Civil y Major Software. He ganado el 100% de las partidas de Ataque que he jugado.
                    </p>
                </div>
                <a href='/'>Volver Atras</a>

            </div>


        </>
    )
}
