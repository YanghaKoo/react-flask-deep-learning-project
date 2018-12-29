import React, { Component } from 'react';
import "./ClassListItem.scss"
import Original from '../Original/Original';
import Product from '../Product/Product';

class ClassListItem extends Component {  
  render() {
    const {label, sresult, id } = this.props        
    let flag = 0;        
    if(!sresult[0]){
      flag = 1;
    }
    return (
      <div className="class-list-item">
        <Original label={label} id={id}/>                
        <Product sresult={sresult} flag={flag}/>  
      </div>
    );
  }
}

export default ClassListItem;