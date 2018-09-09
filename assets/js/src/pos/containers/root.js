import React, {Component} from 'react';
import {SearchableWidget} from '../components/common';
import TextBoxListWidget from '../components/text_box_list';
//import Keypad from '../components/keypad';
import TouchController from './touchController';

class POSRoot extends Component{
    state = {
        trip: "",
        customer_id: "",
        customer_number: "",
        feature_level: "",
        alertNumbers: [] 
    }
    onTripSelect = (data) =>{
        this.setState({trip: data});
    }

    onTripClear = () =>{
        this.setState({trip: ""});
    }

    inputHandler = (evt) =>{
        const name = evt.target.name;
        let newState = this.state;
        newState[name] = evt.target.value; 
        this.setState(newState);
    }

    featureHandler = (evt) =>{
        this.setState({feature_level: evt.target.value})
    }
    render(){
        return(
            <div>
                <h1>Purchase Tracking Token</h1>
                <h3>Select Trip</h3>
                <SearchableWidget
                    dataURL= "/buses/api/trip/"
                    displayField= "name"
                    onSelect={this.onTripSelect}
                    onClear={this.onTripClear}
                    idField="id" />
                <h3>Customer Details</h3>
                <label htmlFor="customer_id">Customer ID</label><br />
                    <input
                        value={this.state.customer_id}
                        onChange={this.inputHandler}
                        name="customer_id"
                        className="form-control"
                        placeholder="enter ID number here..."
                        />
                <label htmlFor="customer_number">Customer Phone Number</label><br />
                    <input 
                        value={this.state.customer_number}
                        onChange={this.inputHandler}
                        name="customer_number"
                        className="form-control"
                        placeholder='enter phone number here...'
                />
                <label htmlFor="customer_number">Tracker Feature Level</label><br />
                <select 
                    onChange={this.featureHandler}
                    className="form-control">
                    <option value="">-------</option>
                    {['basic', 'enhanced', 'ultimate'].map((el, i)=>{
                        return(<option 
                                    key={i} 
                                    value={el}>
                                    {el}    
                                </option>);
                    })}
                </select>

                <h3>Alert Phone Numbers</h3>
                <TouchController />
                <TextBoxListWidget 
                        populatedURL ={null}
                        fieldName="phone_numbers"/>
            </div>
        )
    }
}

export default POSRoot;
