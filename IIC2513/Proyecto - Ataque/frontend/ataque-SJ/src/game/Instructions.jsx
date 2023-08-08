import Example from './Example.jsx'
import ExampleMove from './ExampleMove.jsx'
import './instructions.css'
import ThrownDice from './ThrownDice.jsx'
export default function Instructions() {

    return (
        <>
            <h1>REGLAS DEL JUEGO</h1>
            <p>Risk SJ es un juego creado para un mínimo de 3 participantes y un máximo de 6. Éste es un juego en el que se requiere no sólo suerte, sino también una fuerte dosis de estrategia para resultar vencedor. El juego consiste en <b>conquistar un objetivo determinado.</b></p>
            <h2>ANTES DE EMPEZAR</h2>
            <p>Las fichas utilizadas para este juego se denominan alumnos. Cada facultad tiene un color. Los jugadores deben elegir el color de la facultad con que jugarán. </p>
            <p><b>DISTRIBUIDOR:</b> Para elegir al distribuidor, cada jugador lanzará un dado. El que obtenga mayor puntaje será el distribuidor y estará encargado de repartir las ‘Cartas-Territorio’ y las ‘Cartas-Objetivo’</p>
            <p><b>OBJETIVO:</b> Para conocer el objetivo, cada jugador deberá elegir una ‘Carta-Objetivo’ de entre las presentadas por el distribuidor. Estas cartas estarán dispuestas de manera que no se vea su contenido. En las ‘Cartas-Objetivo’ está indicado, claramente, cuál es el objetivo que debemos conseguir. El jugador que logre su objetivo primero es el ganador. El contenido de las ‘Cartas-Objetivo’ deberá <b>mantenerse en secreto</b> durante todo el juego por su poseedor, y lo dará a conocer sólo en el caso de conseguir el objetivo indicado en ésta, o sea si es ganador (o si el juego termina y otro jugador ha ganado). Es conveniente que los jugadores estén familiarizados con el contenido de las ‘CartasObjetivo’ para poder prever las posibles estrategias de sus compañeros de juego. En el caso de que los participantes sean menos que 6, deberá excluirse del juego aquellas ‘Cartas-Objetivo’ que consideren los colores de los alumnos que no están participando.</p>
            <p><b>TERRITORIOS</b>: Cuando cada jugador haya elegido a su facultad, y los objetivos estén asignados, el distribuidor procederá a repartir las ‘Cartas-Territorio’. El distribuidor tomará el conjunto de las ‘Cartas-Territorio’, barajará las cartas y retirará los dos comodines (cartas que tienen tres figuras geométricas). Distribuirá todas las cartas comenzando por sí mismo, siguiendo por su izquierda. Luego, cada jugador procederá a ocupar sus territorios, colocando en cada uno de los territorios que obtuvo en el sorteo, una facultad. Este facultad se denomina ‘De Ocupación’. En esta etapa todos los territorios deberán quedar ocupados, y así deberán permanecer durante todo el juego. NO PUEDE haber territorios desocupados. Después de que hayan sido ocupados con un facultad todos los territorios, los jugadores devolverán las cartas al distribuidor, quien las unirá a los comodines y las mezclará.</p>
            <h2>EL JUEGO</h2>
            <p>Inicia el jugador siguiente al que recibió la última ‘Carta-Territorio’. En cada ronda de juego, cada jugador recibirá alumnos. La cantidad de éstos se determinará al inicio del turno de juego, contando la cantidad de territorios ocupados por sus facultad y dividiéndolo por 2 (considerándose sólo la parte entera del resultado, en caso de ser impar la cantidad de territorios). EJEMPLO: Si el jugador tiene 9 territorios ocupados, le corresponderá 4 ejercitos. En la primera ronda, el iniciador determinará la cantidad de alumnos que le corresponden. Luego él, y cada jugador, procederán a sacar la cantidad de alumnos calculados, los cuales serán ubicados por cada jugador en los territorios que tengan ocupados, según sea su conveniencia, teniendo en cuenta el objetivo que debe conseguir. Los alumnos serán sacados junto con el jugador que inicia el juego, pero cada jugador los ubicará en el tablero cuando le corresponda el turno de jugar. Sólo en la primera ronda de juego la cantidad de alumnos adicionales estará determinada para todos iguales. En las siguientes rondas, la cantidad de alumnos que le corresponde a cada jugador, estará determinada para cada uno en particular, por la cantidad de territorios que tenga ocupados al iniciar su turno de juego. </p>
            <p><b>OBSERVACIÓN: </b> El mínimo de alumnos a recibir es SIEMPRE 3. Aunque el jugador posea menos de 6 territorios. El jugador en su turno, deberá colocar todos los alumnos recibidos en uno o más de sus territorios, de acuerdo a su estrategia para lograr el objetivo. A continuación, el jugador podrá o no atacar a sus adversarios de acuerdo a su conveniencia.</p>
            <p><b>ATAQUE</b>: Cada territorio debe estar ocupado con, por lo menos, un facultad ‘De Ocupación’, el que NO tiene derecho a atacar. Para hacerlo, se debe contar con, por lo menos, 2 alumnos en el territorio.</p>

            <h2>CONSIDERACIONES Y FUNCIONAMIENTO</h2>
            <p>Una facultad puede atacar solamente a una facultad adversaria con el que tenga fronteras en común, o esté unido por línea de puntos. EJ: Atacar MATEMÁTICAS desde FÍSICA, o viceversa. El jugador podrá atacar con cuantos alumnos posea en su facultad, menos el ‘De Ocupación’. El atacado podrá defenderse con cuantos alumnos posea en su facultad, inclusive el ‘De Ocupación’. El jugador en su turno es libre de atacar, o no, las veces y facultades que desee. El atacante deberá especificar, antes de jugar, a qué facultades atacará y desde cuál lo hará. El ataque y defensa de una facultad se hará a través de dados. Aunque la cantidad de alumnos sea superior, no se podrá atacar o defender con más de tres dados cada vez. Así, si el atacante usa tres alumnos contra uno del defensor, él jugará con tres dados contra uno del defensor La decisión, después de una batalla, de quién gana o pierde alumnos, es hecha de la siguiente forma: se compara el dado mayor del atacante con el dado mayor del defensor; el mayor de ellos gana. En seguida se compara el 2° dado mayor del atacante con el del defensor, y el mayor gana. Lo mismo con el menor de ambos jugadores. El empate es siempre victoria para el defensor. Si el atacante lo deseara, podría atacar a un enemigo con una cantidad de dados inferior a la utilizada para defenderse por el enemigo. EJ: ATACANTE 1 alumnos y DEFENSOR 2 ó 3 alumnos. En este caso, se comparará el dado del atacante con el mayor del defensor; el que obtenga menor puntaje, es el que perderá un ejército. Durante un combate en el que el atacante juega con 2 ó 3 dados, y el defensor con un dado; si el atacante resulta perdedor, éste sacará solamente 1 de sus alumnos.</p>

            <h2>EJEMPLOS DE PARTIDA</h2>
            <h3>1. ATACANTE 4 alumnos, DEFENSOR 3 alumnos</h3>
            <p>El ATACANTE y DEFENSOR jugarán con 3 dados cada uno. Se muestran ordenados de mayor a menor</p>
            <p>ATACANTE:</p>
            <div className='dicethrow'>
                <ThrownDice thrown={3} value={[6,4,2]}/>
            </div>
            <p>DEFENSOR:</p>
            <div className='dicethrow'>
                <ThrownDice thrown={3} value={[5,4,3]}/>
            </div>
            <p>RESULTADOS: ATACANTE ya que 6 es mayor que 5, DEFENSOR ya que 4 es igual a 4, ya en empate gana defensa, DEFENSOR, ya que 3 es mayor que 2</p>
            <p>Como se ve, el atacante pierde dos alumnos, quedando con 2. El defensor pierde 1 ejército, también quedando con 2. El atacante puede decidir continuar el ataque. En esta oportunidad, ambos juegan con dos dados. Se muestran ordenados de mayor a menor</p>
            <p>ATACANTE:</p>
            <div className='dicethrow'>
                <ThrownDice thrown={2} value={[5,1]}/>
            </div>
            <p>DEFENSOR:</p>
            <div className='dicethrow'>
                <ThrownDice thrown={2} value={[4,2]}/>
            </div>
            <p>RESULTADOS: ATACANTE ya que 5 es mayor que 4, ATACANTE ya que 3 es mayor a 2</p>
            <p>El defensor retira sus alumnos, y el atacante avanza con un ejército de ocupación a la facultad conquistada. El ganador puede avanzar con un solo ejército a la facultad conquistada mientras no decida terminar de jugar.</p >
            <p>Una vez que el jugador da por terminado su turno, podrá, voluntariamente, reagrupar sus alumnos, trasladando la cantidad deseada de una facultad a otro contiguo o unido por líneas de puntos, debiendo permanecer siempre en sus facultades de alumnos de ocupación. Un alumno puede ser trasladado una sola vez durante la reagrupación, no pudiendo éste avanzar más de una facultad por jugada. La finalidad de la reagrupación una vez terminada la jugada, es la de resguardar las facultades conquistados, o bien, la de prepararlo para una futura batalla.
            </p>
            <h2>
                Ahora pruebalo tu en este ejemplo de un 1 contra 1!
            </h2>
            <div>
                <Example />
            </div>
            <h2>
                Puedes tambien mover tus ejercitos!
            </h2>
            <ExampleMove />
            <br></br>
            <h2>CAMBIO</h2>
            <h3>1. CartasFacultad</h3>
            <p>Si durante su turno un jugador ha logrado conquistar al menos una facultad, tendrá derecho al final de su turno a recibir como premio una carta del mazo de cartasfacultad. En esta oportunidad deberán tomarse en cuentas las figuras geométricas que cada una de estas cartas contiene a uno de sus costados. El jugador deberá juntar tres cartas con figuras geométricas iguales o tres distintas para lograr un CAMBIO (podrá hacer uso de un comodín, carta que contiene 3 figuras). Al juntar las tres figuras, el jugador, al inicio de su turno, deberá entregarlas al Distribuidor, el que las separa del juego. Consultando la tabla I CAMBIO, recibirá determinada cantidad de alumnos extra, dependiendo de la cantidad de veces que haya logrado el cambio. Aquel jugador que en su turno no haya logrado conquistar ninguna facultad, no recibirá carta-facultad hasta que lo logre en sus próximos turnos. Si al cambiar las cartas el jugador posee alguno de las facultades que en ella se indica, tendrá derecho a recibir dos alumnos más, los que deberá colocar obligatoriamente en esa facultad. Si durante el juego un jugador elimina completamente los alumnos de un enemigo, sin ser éste su objetivo, las cartas-facultad del derrotado pasan automáticamente al poder del jugador que lo ha eliminado.</p>

            <h3>2. ZONAS</h3>

            <p>Si al comienzo o a lo largo del juego un jugador posee una zona completa, entonces éste recibirá al comienzo de cada ronda que lo mantenga una cantidad extra de alumnos especificada a un extremo del tablero en la TABLA. Estos alumnos recibidos, deben ser ubicados obligatoriamente dentro de la zona poseído.</p>

            <h2>FINAL DEL JUEGO</h2>
            <p> El juego finaliza cuando un jugador logra alcanzar su objetivo. En ese momento, descubre su carta-objetivo al resto de los jugadores, comprobando su victoria.</p>

            <h2>RESUMEN</h2>
            <p>Cada jugador, en su turno, debe pasar por las siguientes fases: </p>
            <p>1- Recepción de nuevos alumnos (sumando sus facultades y dividiendo por dos. Utilizando otras técnicas que estén a su alcance: cambios, continentes, facultades). </p>
            <p>2- Ubicación de estos alumnos (de acuerdo a su objetivo). </p>
            <p>3- Ataque a otros facultades (si lo desea).</p>
            <p> 4- Reagrupación de los alumnos (si lo desea). </p>
            <p>5- Recibir carta-territorio (si ha logrado conquistar un territorio).
            </p>
            <a href='/pagina-principal'>Volver Atras</a>










        </>
    )
}
