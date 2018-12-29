import React, { Component } from "react";
import "./Product.scss";
import ProductItem from "../ProductItem";

class Product extends Component {

  render() {
    const { sresult, flag, } = this.props;    
    if(flag===1){
      return(
        <div className="no-content">No Content</div>
      )
    }
        
    const list = sresult.map(item => {
               
      return (        
        <ProductItem
          src={item.img}
          title={item.title}
          key={item.img}
          isChecked={item.is_check}
          price={item.price}
          link={item.link}
          noContent={flag}
        />
      );
    });           

    return (
      <div className="product" id="scrollStyle">                
        {list}        
      </div>
    );
  }
}

export default Product