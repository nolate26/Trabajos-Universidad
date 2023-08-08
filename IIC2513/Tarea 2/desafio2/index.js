const fs = require('fs'); // importamos las biblioteca para trabajar con los archivos del sistema
const path = require('path'); // importamos libreria para trabajar con el manejo de path
const prompt = require('prompt-sync')(); // librería para el manejo de los inputs

const abecedario = 'aábcdeéfghiíjklmnñoópqrstuúüvxyz'; // Se define el abecedario a usar

// recibe una palabra,número y la encripta según lo pedido
function encriptar(palabra, numero) {
  let resultado = '';
  for (let i = 0; i < palabra.length; i += 1) { // recorremos la palabra
    const letra = palabra[i]; // la guardamos

    if (!abecedario.includes(letra)) { // si no pertenece al abecedario se agrega así no mas
      resultado += letra;
    } else {
      const indice = abecedario.indexOf(letra); // se consigue el indice
      const nuevaIndice = (indice + numero) % abecedario.length;
      // se suma y si se pasa se comienza del 0
      resultado += abecedario[nuevaIndice];
    }
  }

  return resultado;
}

function procesarArchivo(rotacion, rutaRelativa, nombreArchivo) {
  // guardo la ruta
  const rutaAbsoluta = path.join(__dirname, rutaRelativa, `${nombreArchivo}.txt`);

  // reviso si existe tal ruta relativa
  fs.access(rutaAbsoluta, fs.constants.F_OK, (error) => {
    if (error) {
      console.error(`Error: El archivo ${nombreArchivo}.txt no existe en la ruta ${rutaRelativa}.`);
      codigoPrincipal();
      return;
    }
    // reviso si se leyo el archivo correctamente
    fs.readFile(rutaAbsoluta, 'utf8', (error2, contenido) => {
      if (error2) {
        console.error(`Error al leer el archivo: ${error2.message}`);
        return true;
      }

      // encripto el contenido del archivo y lo guardo
      const contenidoTransformado = encriptar(contenido, rotacion);
      // creo el archivo donde lo colocaré
      const nombreArchivoCifrado = `${nombreArchivo}_cifrado.txt`;

      // creo la nueva ruta
      const rutaAbsolutaCifrado = path.join(__dirname, rutaRelativa, nombreArchivoCifrado);

      // escribo el contenido dado la ruta y nuevo nombre del archivo
      fs.writeFile(rutaAbsolutaCifrado, contenidoTransformado, 'utf8', (error1) => {
        if (error1) {
          console.error(`Error al escribir en el archivo: ${error.message}`);
          return true;
        }

        console.log(`Archivo ${nombreArchivoCifrado} creado exitosamente.`);
        return true;
      });
      return true;
    });
  });
}

function codigoPrincipal() { // creamos la función que corre el código y revisa el input
  const numero = parseInt(prompt('Número a rotar: '), 10); // input numero

  if (isNaN(numero)) { // revisa que sea un número
    console.log('Error: el valor ingresado no es un número entero. Por favor, intenta nuevamente.');
    codigoPrincipal();
    return; // Termina la ejecución de la función actual para evitar la continuación del flujo
  }

  // inputs de rutas y archivos
  const rutaRelativa = prompt('Ruta relativa del archivo: ');
  const archivo = prompt('Archivo a encriptar: ');

  // se procesan
  procesarArchivo(numero, rutaRelativa, archivo);
}

codigoPrincipal(); // corremos el códigos
