import React, { Component } from "react";
import "./ProductItem.scss";
import { connect } from "react-redux";
import * as dataActions from "store/modules/datas";
import { bindActionCreators } from "redux";

class ProductItem extends Component {
  state = {
    isChecked: 0
  };

  handleText = (text) => {
    // <b></b> 태그, %amp;와 같은 불필요한 것들을 정규표현식으로 제거함
    text = text.replace(/<\/?b>/g, "").replace(/&.*;/, "");
    const len = text.length   

    if(len < 35){
      return text
    }else{
      return text.slice(0,30) + "..."
    }
  }

  // 숫자에 3자리마다 ,를 찍어서 보여주는 정규표현식
  numberWithCommas = x => {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  };

  componentWillMount() {
    const { isChecked } = this.props;
    if (isChecked === 1) {
      this.setState({
        isChecked
      });
    }
  }

  handleClick = e => {
    const { handlePrice } = this.props.DataActions;
    const { price } = this.props;

    if (this.state.isChecked) {
      handlePrice(-price);
    } else {
      handlePrice(price);
    }
    this.setState({
      isChecked: !this.state.isChecked
    });
  };

  render() {
    const { src, title, price, link } = this.props;
    const style = this.state.isChecked ? { background: "#443f3d" } : null;
    return (
      <div
        style={style}
        className="product-list-item"
        onClick={this.handleClick}
      >
        <div>
          <img src={src} width="250px" height="250px" alt={title} />
        </div>
        <div className="middle">
          <p>{this.handleText(title)}</p>          
          <p>\ {this.numberWithCommas(price)}</p>
          <a href={link} className="go-shop" target="_blank" rel="noopener noreferrer" style={{fontWeight : "700"}}>
            Get info
          </a>
        </div>
      </div>
    );
  }
}

export default connect(
  null,
  dispatch => ({ DataActions: bindActionCreators(dataActions, dispatch) })
)(ProductItem);
