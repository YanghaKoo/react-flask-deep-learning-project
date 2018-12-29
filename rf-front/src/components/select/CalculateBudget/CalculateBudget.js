import React, { Component } from 'react';
import './CalculateBudget.scss'

class CalculateBudget extends Component {
  numberWithCommas =(x) =>{
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  }  
  
  render() {
    const {budget, currentPrice} = this.props
    let style= null
    if( budget >0 && budget <= currentPrice){
      style = {color : "red"}
    }
    
    let bg;
    if(budget <=0){
      bg  = "Budget Unprovided"
    }else{
      bg = "Your Budget : \\" + this.numberWithCommas(budget)
    }
    return (
      <div className="calculate-budget">
        <div className="budget">
          {bg}
        </div>
        <div className="current" style={style}>
          Total : \{this.numberWithCommas(currentPrice)}
        </div>        
      </div>
    );
  }
}
export default CalculateBudget;