import { useState } from "react";
import "./App.css";

function App() {
  // definimos los estados
  const [expresion, setExpresion] = useState("");
  const [operador, setOperador] = useState("");
  const [isOperadorSelected, setIsOperadorSelected] = useState(false);
  const [isMostrarResultado, setisMostrarResultado] = useState(false);
  const [contadorMenos, setContadorMenos] = useState(0);

  // función al apretar operación o número
  const botonClick = (value) => {

    // reiniciar al pulsar luego de dar resultado
    if (isMostrarResultado) {
      if (/^[+\-*÷]+$/.test(value)) {
        botonReiniciar() // limpiamos
        setisMostrarResultado(false); // quitamos estado
        return;
      }
      // mismo caso para numeros
      else if (/^[0-9]+$/.test(value)) {
        botonReiniciar();
        setisMostrarResultado(false);
      }
    }

    // Revisar que sea número válido
    if (/^[0-9]+$/.test(value)) {
      setExpresion((operacionPrevia) => operacionPrevia + value);
    }
    else if (/^[+\*÷]+$/.test(value) && !isOperadorSelected) {
      // Validar semántica de la operación 
      if (value === "*" && expresion === "") {
        return;
      }
      if (value === "÷" && expresion === "") {
        return;
      }
      if (value === "+" && expresion === "") {
        return;
      }
      setOperador(value);
      setExpresion((operacionPrevia) => operacionPrevia + value);
      setIsOperadorSelected(true);
    }

    else if (/^[-]+$/.test(value) && expresion === "") {
      setExpresion((operacionPrevia) => operacionPrevia + value);
      setContadorMenos((operacionPrevia) => operacionPrevia + 1);

    }
    else if (/^[-]+$/.test(value) && contadorMenos < 2 && expresion[expresion.length - 1] != "-") {
      if (!isOperadorSelected) {
        setOperador(value);
        setIsOperadorSelected(true);
      }

      setExpresion((operacionPrevia) => operacionPrevia + value);
      setContadorMenos((operacionPrevia) => operacionPrevia + 1);
    }

  };


  const botonReiniciar = () => {
    setExpresion("");
    setOperador("");
    setIsOperadorSelected(false);
    setContadorMenos(0);
  };

  const botonBorrar = () => {
    if (isMostrarResultado) {
      botonReiniciar()
      setisMostrarResultado(false);
    }
    else if (/^[+\-*÷]+$/.test(expresion[expresion.length - 1])) {
      setIsOperadorSelected(false);
      setOperador("");
    }
    else if (/^[-]+$/.test(expresion[expresion.length - 1])) {
      setIsOperadorSelected(false);
      setOperador("");
      setContadorMenos((operacionPrevia) => operacionPrevia - 1);
    }
    setExpresion((operacionPrevia) => operacionPrevia.slice(0, -1));
  };

  const botonCalcular = () => {

    // no hace nada si no hay operador
    if (!isOperadorSelected) {
      return;
    }
    // Creado con chatgpt (el elegir operador)
    const lastIndex = expresion.lastIndexOf(operador);
    if (lastIndex === -1) {
      // No se encontró el operador en la expresión
      return;
    }

    const operador1 = expresion.substring(0, lastIndex);
    const operador2 = expresion.substring(lastIndex + operador.length);
    // retornar si no hay argumentos en operadores
    if (operador1 === '') {
      return;
    }
    if (operador2 === '') {
      return;
    }

    let operacionPedida = '';

    // Mapear el operador a su equivalente en la solicitud Fetch
    switch (operador) {
      case '+':
        operacionPedida = 'suma';
        break;
      case '*':
        operacionPedida = 'mult';
        break;
      case '÷':
        operacionPedida = 'div';
        break;
      case '-':
        operacionPedida = 'resta';
        break;
      default:
        break;
    }

    // obtenido el operador y que sea posible ejecutar la operacion
    // Hacemos GET o POST según es pedido
    let url = "";
    let bodyData = null;
    let method = "";
    // Verifica si el operador es "-" o "÷"
    if (operador === "-" || operador === "÷") {
      // Si es "-" o "÷", utiliza el método POST
      url = `http://localhost:3000/${operacionPedida}`;
      method = "POST";
      bodyData = {
        operand1: operador1,
        operand2: operador2,
      };
      fetch(url, {
        method,
        headers: {
          "Content-Type": "application/json", // Establece el tipo de contenido como JSON
        },
        body: JSON.stringify(bodyData), // Convierte el objeto payload a una cadena JSON
      })
        .then((response) => {
          if (response.ok) {
            return response.text();
          } else {
            throw new Error("dividir por 0");
          }
        })
        .then((text) => {
          setisMostrarResultado(true);
          setExpresion(text);
          setOperador("");
          setIsOperadorSelected(false);
          setContadorMenos(0);
        })
        .catch((error) => {
          console.error(error);
          setExpresion("Error: " + error.message);
          setisMostrarResultado(true);
          setOperador("");
          setIsOperadorSelected(false);
          setContadorMenos(0);
        });
    } else {
      url = `http://localhost:3000/${operacionPedida}/${operador1}/${operador2}`;
      // Si es otro operador, utiliza el método GET
      method = "GET";
      fetch(url, { method })
        .then((response) => {
          if (response.ok) {
            return response.text();
          } else {
            throw new Error("dividir por 0");
          }
        })
        .then((text) => {
          setisMostrarResultado(true)
          setExpresion(text);
          setOperador("");
          setIsOperadorSelected(false);
          setContadorMenos(0);
        })
        .catch((error) => {
          // Manejar el error de la solicitud
          console.error(error);
          // Mostrar el mensaje de error al usuario
          setExpresion("Error: " + error.message);
          setisMostrarResultado(true);
          setOperador("");
          setIsOperadorSelected(false);
          setContadorMenos(0);
        });
    }
  };

  return (
    <div className="calculator-grid">
      <div className="output">
        <div className="current-operand">{expresion}</div>
      </div>
      <button className="span-two" onClick={botonReiniciar}>
        AC
      </button>
      <button onClick={botonBorrar}>DEL</button>
      <button onClick={() => botonClick("÷")}>÷</button>
      <button onClick={() => botonClick("1")}>1</button>
      <button onClick={() => botonClick("2")}>2</button>
      <button onClick={() => botonClick("3")}>3</button>
      <button onClick={() => botonClick("*")}>*</button>
      <button onClick={() => botonClick("4")}>4</button>
      <button onClick={() => botonClick("5")}>5</button>
      <button onClick={() => botonClick("6")}>6</button>
      <button onClick={() => botonClick("+")}>+</button>
      <button onClick={() => botonClick("7")}>7</button>
      <button onClick={() => botonClick("8")}>8</button>
      <button onClick={() => botonClick("9")}>9</button>
      <button onClick={() => botonClick("-")}>-</button>
      <button></button>
      <button onClick={() => botonClick("0")}>0</button>
      <button className="span-two" onClick={botonCalcular}>
        =
      </button>
    </div>
  );
}

export default App;

