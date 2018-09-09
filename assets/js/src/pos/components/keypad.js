import React from 'react';

const buttonLabels = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
    ['00', '0', '.'],
];

const keypad = (props) => {
    return(<div>
        {buttonLabels.map((row, i) =>{
            return(
                <div style={{margin: "5px"}}>        
                    {row.map((label, j) => {
                        return(<button 
                                    className="btn"
                                    style={{
                                        marginLeft: "5px",
                                        minWidth: "50px"
                                    }}>{label}</button>)})}
                </div>
            )
        })}
    </div>);
}

export default keypad;