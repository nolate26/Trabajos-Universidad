import React, { useState, useEffect } from "react";
import './Army.css';


function Army(props) {
  const [clicked, setClicked] = useState(false);
  useEffect(() => {
    if (clicked) {
      setClicked(false);
      props.clicked(props.value, props.armies, props.color);
    }
  }, [clicked]);

    const mystyle = {
        left: props.left,
        top: props.top,
        backgroundColor: props.color
      };

  return (
    <div id={props.value} className="Army" style={mystyle} onClick={() => {setClicked(true)}}>
        <p>{props.armies}</p>
    </div>
  );

}

export default Army;
