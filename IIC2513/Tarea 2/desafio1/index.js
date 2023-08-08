const { abrirSistemas, restriccionesSanitarias, emiteCertificado, cerrarSistemas } = require('./planificacion.js');
const prompt = require('prompt-sync')(); // librería para el manejo de los inputs
const destinos = [{ codigo: 'CEV87', ciudad: 'Buenos Aires', restricciones: 36 },
  { codigo: 'SIP23', ciudad: 'Santiago', restricciones: 20 },
  { codigo: 'HVN99', ciudad: 'Lima', restricciones: 10 },
  { codigo: 'KCE98', ciudad: 'Sao Paulo', restricciones: 50 },
  { codigo: 'DCN29', ciudad: 'Bogota', restricciones: 22 },
  { codigo: 'RMM83', ciudad: 'Caracas', restricciones: 15 },
  { codigo: 'TGN24', ciudad: 'Montevideo', restricciones: 30 },
  { codigo: 'KST42', ciudad: '', restricciones: 92 },
  { codigo: 'QQW58', ciudad: 'Asuncion', restricciones: 83 }];

function revisarInput(string) {
  if (string.length !== 5) {
    console.log('Error: El string no tiene 5 caracteres');
    return false; // No cumple con la longitud de 5 caracteres
  }
  const letrasMayusculas = /^[A-Z]+$/;
  const numeros = /^[0-9]+$/;

  const primerosTres = string.substring(0, 3);
  const ultimosDos = string.substring(3, 5);

  if (!letrasMayusculas.test(primerosTres)) {
    console.log('Error: Los primeros tres caracteres no son letras mayúsculas');
    return false; // Los primeros tres caracteres no son letras mayúsculas
  }

  if (!numeros.test(ultimosDos)) {
    console.log('Error: Los últimos dos caracteres no son números');
    return false; // Los últimos dos caracteres no son números
  }

  return true; // Cumple con todas las condiciones
}

function buscarDestino(codigo) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const destinoEncontrado = destinos.find(destino => destino.codigo === codigo);

      if (destinoEncontrado) {
        resolve(destinoEncontrado);
      } else {
        reject('El destino no se encuentra.');
      }
    }, 2000);
  });
}

function codigoPrincipal() {
  const codigo = prompt('Código de destino: '); // primero se recibe el código de destino
  let input = revisarInput(codigo); // se revisa si es correcto
  if (!input) { // si es erroneo se vuelve a pedir
    codigoPrincipal();
    return;
  }

  // ahora lo conectamos al sistema usando la función abrirSistemas
  abrirSistemas(4000)

    // Al terminar de abrir el sistema se busca el Destino
    .then(() => {
      return buscarDestino(codigo);
    })

    // Si se encuentra destino
    .then(resultado => {
      return restriccionesSanitarias(resultado.restricciones, resultado.ciudad);
    })

    // Se realiza búsqueda de las restricciones sanitarias
    .then(respuesta => {
      // Si el viaje es válido
      console.log(`Sin restricciones sanitarias a destino: ${respuesta.destino}`);
      return emiteCertificado(respuesta.destino); // Llamada emiteCertificado
    })
    // Si realiza la emisión del certificado
    .then(resultadoCertificado => {
      console.log(resultadoCertificado.status);
      cerrarSistemas(); // cerramos el sistema
    })
    .catch(error => {
      console.error(error);
      cerrarSistemas();
    });
}

codigoPrincipal();
