import React, { useState } from 'react';
import './dice.css';

export default function Dice(props){
  if (props.draw === 1){
    return(
    <div className="dice face-1">
    </div>

    )} else if (props.draw === 2){
    return(
    <div className="dice face-2">
    </div>

    )} else if (props.draw === 3){
    return(
    <div className="dice face-3">
    </div>

    )} else if (props.draw === 4){
    return(
    <div className="dice face-4">
    </div>

    )} else if (props.draw === 5){
    return(
    <div className="dice face-5">
    </div>

    )} else if (props.draw === 6){
    return(
    <div className="dice face-6">
    </div>
    )}
  }

