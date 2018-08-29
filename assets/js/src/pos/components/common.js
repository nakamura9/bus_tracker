import React, {Component} from 'react';
import PropTypes from 'prop-types';
import axios from 'axios';

export const Aux = (props) => props.children;

const DeleteButton = (props) => {
        return(
            <button
                className="btn btn-danger"
                type="button"
                onClick={() => (props.handler(props.index))}>
                <i className="fas fa-trash"></i>
            </button>
        );
    }

DeleteButton.propTypes = {
    handler: PropTypes.func.isRequired,
    index: PropTypes.number.isRequired
}

class Totals extends Component{
    state = {
        taxObj: null,
        tax: 0.00,
        subtotal: 0.00,
        total: 0.00
    }
    componentDidMount(){
        //get sales tax
        axios({
            method: "GET",
            url: "/invoicing/api/config/1"
        }).then(res =>{
            this.setState({taxObj: res.data.sales_tax})
        })
    }
    componentDidUpdate(prevProps, prevState){
        if(prevProps.list !== this.props.list){
            //update totals 
            let subtotal = this.props.list.reduce(this.props.subtotalReducer, 0);
            
            let taxAmount;
            if(this.state.taxObj){
                taxAmount = subtotal * (this.state.taxObj.rate / 100);
            }else{
                taxAmount = 0.0;
            }
            let total = subtotal + taxAmount;
            this.setState({
                subtotal : subtotal,
                tax : taxAmount,
                total : total
            });
        }
    }
    render(){
        let contents;
        if(this.state.tax === null){
            contents = (
                <tfoot>
                    <tr>
                        <th colSpan={this.props.span - 1}>Total</th>
                        <td>{this.state.total}</td>
                    </tr>
                </tfoot>
            )
        }else{
            contents = (
                <tfoot>    
                    <tr>
                            <th colSpan={this.props.span - 1}>Subtotal</th>
                            <td>{this.state.subtotal.toFixed(2)}</td>
                        </tr>
                        <tr>
                            <th colSpan={this.props.span - 1}>Tax</th>
                            <td>{this.state.tax.toFixed(2)}</td>
                        </tr>
                        <tr>
                            <th colSpan={this.props.span - 1}>Total</th>
                            <td>{this.state.total.toFixed(2)}</td>
                        </tr>
                </tfoot>
                )
        }
        return(contents);
    }
}

Totals.propTypes = {
    span: PropTypes.number.isRequired,
    list: PropTypes.array.isRequired,
    subtotalReducer: PropTypes.func.isRequired
}

class SearchableWidget extends Component {
    //currValue is whats being typed, selected is the value validated
    state = {
        items: [],
        choices: [],
        currValue: "",
        selectedValue: ""
    }

    componentDidMount(){
        axios({
            method: "GET",
            url: this.props.dataURL
        }).then(res => {
            let newChoices = res.data.map((item) =>{
                return(item[this.props.idField] + " - " + item[this.props.displayField])
            });

            this.setState({
                items: res.data,
                choices: newChoices
            });
        })
    }

    handleChange = (evt) => {
        let selectedValue = "";
        let index = this.state.choices.indexOf(evt.target.value);
        
        if(index !== -1){
            selectedValue = evt.target.value;

        }
        this.setState({
            currValue: evt.target.value,
            selectedValue: selectedValue
        });
        if(index !== -1){
            this.props.onSelect(evt.target.value);
        }
    }
    render(){
        let rendered;
        if(this.state.selectedValue === ""){
            rendered = (
                <input 
                    type="text"
                    className="form-control"
                    value={this.state.currValue}
                    onChange={this.handleChange}
                    placeholder="Select item..."
                    list="id_list"/>
            )
        }else{
            rendered = (
                <div style={{
                    width:'100%', 
                    margin: '0px', 
                    minHeight: '35px',
                    backgroundColor: '#ccc'
                }} >
                    <span>{this.state.selectedValue}</span>
                    <span style={{float:'right'}}>
                        <button 
                            style={{
                                backgroundColor: '#',
                                color: 'white',
                                border: '0px',
                                boxShadow: 'none',
                                minHeight: '35px',
                                minWidth: '35px'
                            }}
                            onClick={() =>{
                                this.setState({
                                    selectedValue: "",
                                    currValue: ""
                                });
                                this.props.onClear();
                            }}>
                            <i className="fas fa-times"></i>
                        </button>
                    </span>
                </div>
            )
        }
        return(
            <div>
                {rendered}   
                <datalist id="id_list">
                    {this.state.items.map((item, i) => {
                        //always display id and display field
                        return(<option key={i} >
                                {item[this.props.idField]} - {item[this.props.displayField]}
                            </option>)
                    })}
                    
                </datalist>
            </div>
        );
    }
}

SearchableWidget.propTypes = {
    dataURL: PropTypes.string.isRequired,
    displayField: PropTypes.string.isRequired,
    onSelect: PropTypes.func.isRequired,
    onClear: PropTypes.func.isRequired,
    idField: PropTypes.string.isRequired

}


class AsyncSelect extends Component{
    state = {
        options: []
    }
    componentDidMount(){
        axios({
            method: "GET",
            url: this.props.dataURL
        }).then(res => {
            const dataList = this.props.resProcessor(res);
            this.setState({options: dataList});
        }
            )
    }
    render(){
        return(
            <select 
                onChange={(evt) => this.props.handler(evt.target.value)}
                className="form-control">
                <option value="">-------</option>
                {this.state.options.map((opt, i) =>{
                    return(<option 
                                value={opt.value}
                                key={i}>{opt.name}</option>)
                })}
            </select>
        )
    }
}

AsyncSelect.propTypes = {
    dataURL: PropTypes.string.isRequired,
    resProcessor: PropTypes.func.isRequired,
    handler: PropTypes.func.isRequired,
}
export {DeleteButton, Totals, SearchableWidget, AsyncSelect};