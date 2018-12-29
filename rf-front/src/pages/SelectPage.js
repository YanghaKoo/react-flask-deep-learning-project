import React, { Component } from 'react';
import ClassListContainer from '../containers/ClassListContainer';
import CalculateBudgetContainer from '../containers/CalculateBudgetContainer';
import { connect } from 'react-redux'


class SelectPage extends Component {
  
  
  render() {
    if(this.props.currentPrice < 0){
      return (
        <div>
          잘못된 접근입니다.
        </div>
      )
    }
    return (
      <div className="clc">        
        <ClassListContainer/>
        <CalculateBudgetContainer/>
      </div>
    );
  }
}

export default connect(
  state => {
    return ({current : state.datas.currentPrice})
  }
)(SelectPage)