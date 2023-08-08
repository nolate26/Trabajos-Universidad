// Biblioteca planificacion.js


function abrirSistemas(delay) {
  // Si lo desea este código puede modificarse

  /* La funcion recibe como parametro un “delay” que es la cantidad de milisegundos que demorará el sistema en abrirse
  delay DEBE ser mayor o igual a 3300
  */
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      console.log("Puede iniciar el proceso");
      resolve();
    }, delay);

  })

}
function cerrarSistemas() {
  //No se modifica el código
  console.log("sistemas cerrados de forma segura");
}

function restriccionesSanitarias(restriccion, destino) {
  /*Modifique el código para manejar la restricción.
  Recuerde que restricción es un entero, por ende lo que está en este código es referencial, sin embargo NO MODIFIQUE ni setTimeout ni el retorno de una promesa. Solo intervenga la función callback de setTimeout*/

  return new Promise((resolve, reject) => {
    setTimeout(() => {

      const numero_generado = Math.floor(Math.random() * (100 - 10)) + 10;

      if (numero_generado < restriccion) { // no hubo restriccion
        const objReturn = {};
        objReturn.valid = true; // el viaje es valido
        objReturn.destino = destino;
        resolve(objReturn); // resolvemos la promesa

      } else {
        const objReturn = {}; // hubo restriccion
        objReturn.valid = false; // el viaje no es valido
        reject("Hay restricciones de viaje, no puede viajar");; // rechazamos la promesa
      }

    }, 3353);//randomGenerado es el número que usted genera y que comparado con el parámetro restriccion genera un rechazo.
  })
}

function emiteCertificado(destino) {

  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (destino != '') {
        const objReturn = {};
        objReturn.certificado = true;
        objReturn.status = "Certificado emitido para destino " + destino;
        resolve(objReturn);
      }

      else reject("error en emisión");

    }, 3103);
  })
}
module.exports = {
  abrirSistemas,
  cerrarSistemas,
  restriccionesSanitarias,
  emiteCertificado
};