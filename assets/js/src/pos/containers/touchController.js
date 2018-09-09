import React, {Component} from 'react';
import Keypad from '../components/keypad';

export default class TouchController extends Component{
    render(){
        return(
            <div>
                <div>
                    <input className="form-control"/>
                </div>
                <div>
                    <Keypad />
                </div>
            </div>
        )
    }
}

