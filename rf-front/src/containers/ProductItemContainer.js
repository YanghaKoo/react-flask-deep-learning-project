import React, { Component } from 'react';
import ProductItem from '../components/select/ProductItem/ProductItem';
import { connect } from 'react-redux'
import * as dataActions from 'store/modules/datas'
import { bindActionCreators } from 'redux';

class ProductItemContainer extends Component {
  render() {
    console.log(this.props)
    return (
      <div>
        <ProductItem DataActions={this.props.DataActions}/>
      </div>
    );
  }
}

export default connect(
  null,
  dispatch => ({DataActions :bindActionCreators(dataActions,dispatch)})
)(ProductItemContainer)