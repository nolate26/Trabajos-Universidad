import React, { useState } from 'react';
import './ThrowDice.css';
import Dice from './dice.jsx';

export default function ThrownDice(props) {
  if (props.thrown === 1) {
    return (
      <div className="throw t1">
        <Dice draw={props.value[0]} />
      </div>
    )
  } else if (props.thrown === 2) {
    return (
      <div className="throw t2">
        <Dice draw={props.value[0]} />
        <Dice draw={props.value[1]} />
      </div>
    )
  } else if (props.thrown === 3) {
    return (
      <div className="throw t3">
        <Dice draw={props.value[0]} />
        <Dice draw={props.value[1]} />
        <Dice draw={props.value[2]} />
      </div>
    )
  }
}
