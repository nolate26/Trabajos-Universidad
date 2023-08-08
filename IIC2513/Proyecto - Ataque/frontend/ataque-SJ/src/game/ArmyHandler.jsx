import React, { useEffect, useState } from "react";
import Army from './Army.jsx';

function ArmyHandler(props) {
    const [boardState, setBoardState] = useState(Array(26).fill([[0,0],0,0]))
    const [clickValue, setClickValue] = useState('');
    useEffect(() => {
        if (props.gameState.players == undefined) {
            return;
        }
        let newBoardState = Array(26).fill(0).map((_, i) => {
            return describeTerritory(i, props.gameState.players);
        })
        setBoardState(newBoardState);
    }, [props.gameState]);

    function checkClickedValue (value, armies, color) {
        setClickValue(value, armies, color);
        props.clicked(value, armies, color);
    }
  return (
    <div>
        <Army value='1' armies={boardState[0][2]} left={boardState[0][0][0]} top={boardState[0][0][1]} color={boardState[0][1]} clicked={checkClickedValue} />
        <Army value='2' armies={boardState[1][2]} left={boardState[1][0][0]} top={boardState[1][0][1]} color={boardState[1][1]} clicked={checkClickedValue} />
        <Army value='3' armies={boardState[2][2]} left={boardState[2][0][0]} top={boardState[2][0][1]} color={boardState[2][1]} clicked={checkClickedValue} />
        <Army value='4' armies={boardState[3][2]} left={boardState[3][0][0]} top={boardState[3][0][1]} color={boardState[3][1]} clicked={checkClickedValue} />
        <Army value='5' armies={boardState[4][2]} left={boardState[4][0][0]} top={boardState[4][0][1]} color={boardState[4][1]} clicked={checkClickedValue} />
        <Army value='6' armies={boardState[5][2]} left={boardState[5][0][0]} top={boardState[5][0][1]} color={boardState[5][1]} clicked={checkClickedValue} />
        <Army value='7' armies={boardState[6][2]} left={boardState[6][0][0]} top={boardState[6][0][1]} color={boardState[6][1]} clicked={checkClickedValue} />
        <Army value='8' armies={boardState[7][2]} left={boardState[7][0][0]} top={boardState[7][0][1]} color={boardState[7][1]} clicked={checkClickedValue} />
        <Army value='9' armies={boardState[8][2]} left={boardState[8][0][0]} top={boardState[8][0][1]} color={boardState[8][1]} clicked={checkClickedValue} />
        <Army value='10' armies={boardState[9][2]} left={boardState[9][0][0]} top={boardState[9][0][1]} color={boardState[9][1]} clicked={checkClickedValue} />
        <Army value='11' armies={boardState[10][2]} left={boardState[10][0][0]} top={boardState[10][0][1]} color={boardState[10][1]} clicked={checkClickedValue} />
        <Army value='12' armies={boardState[11][2]} left={boardState[11][0][0]} top={boardState[11][0][1]} color={boardState[11][1]} clicked={checkClickedValue} />
        <Army value='13' armies={boardState[12][2]} left={boardState[12][0][0]} top={boardState[12][0][1]} color={boardState[12][1]} clicked={checkClickedValue} />
        <Army value='14' armies={boardState[13][2]} left={boardState[13][0][0]} top={boardState[13][0][1]} color={boardState[13][1]} clicked={checkClickedValue} />
        <Army value='15' armies={boardState[14][2]} left={boardState[14][0][0]} top={boardState[14][0][1]} color={boardState[14][1]} clicked={checkClickedValue} />
        <Army value='16' armies={boardState[15][2]} left={boardState[15][0][0]} top={boardState[15][0][1]} color={boardState[15][1]} clicked={checkClickedValue} />
        <Army value='17' armies={boardState[16][2]} left={boardState[16][0][0]} top={boardState[16][0][1]} color={boardState[16][1]} clicked={checkClickedValue} />
        <Army value='18' armies={boardState[17][2]} left={boardState[17][0][0]} top={boardState[17][0][1]} color={boardState[17][1]} clicked={checkClickedValue} />
        <Army value='19' armies={boardState[18][2]} left={boardState[18][0][0]} top={boardState[18][0][1]} color={boardState[18][1]} clicked={checkClickedValue} />
        <Army value='20' armies={boardState[19][2]} left={boardState[19][0][0]} top={boardState[19][0][1]} color={boardState[19][1]} clicked={checkClickedValue} />
        <Army value='21' armies={boardState[20][2]} left={boardState[20][0][0]} top={boardState[20][0][1]} color={boardState[20][1]} clicked={checkClickedValue} />
        <Army value='22' armies={boardState[21][2]} left={boardState[21][0][0]} top={boardState[21][0][1]} color={boardState[21][1]} clicked={checkClickedValue} />
        <Army value='23' armies={boardState[22][2]} left={boardState[22][0][0]} top={boardState[22][0][1]} color={boardState[22][1]} clicked={checkClickedValue} />
        <Army value='24' armies={boardState[23][2]} left={boardState[23][0][0]} top={boardState[23][0][1]} color={boardState[23][1]} clicked={checkClickedValue} />
        <Army value='25' armies={boardState[24][2]} left={boardState[24][0][0]} top={boardState[24][0][1]} color={boardState[24][1]} clicked={checkClickedValue} />
        <Army value='26' armies={boardState[25][2]} left={boardState[25][0][0]} top={boardState[25][0][1]} color={boardState[25][1]} clicked={checkClickedValue} />
    </div>

  );

}
function describeTerritory(id, players){
    let position = ArmyPositions[id];
    id += 1;
    let color = 'white';
    let armies = 1;
    players.forEach(player => {
        player.territories.forEach(territory => {
            if (territory.id == id) {
                color = player.color  ;
                armies = territory.armies;
            }
        })
    })
    return [position, color, armies  ]
}
const ArmyPositions = [
    [155, 325],
    [250, 325],
    [190, 245],
    [285, 245],
    [420, 200],
    [470, 305],
    [570, 400],
    [555, 300],
    [480, 400],
    [540, 210],
    [600, 190],
    [690, 150],
    [775, 235],
    [720, 285],
    [630, 290],
    [740, 345],
    [775, 460],
    [830, 590],
    [735, 590],
    [510, 485],
    [510, 560],
    [370, 530],
    [400, 420],
    [245, 460],
    [165, 440],
    [260, 390]
]
export default ArmyHandler;
