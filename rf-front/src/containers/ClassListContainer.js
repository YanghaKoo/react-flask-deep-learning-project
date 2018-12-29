import React, { Component } from 'react';
import {connect} from 'react-redux'
import ClassList from '../components/select/ClassList';
import * as dataActions from 'store/modules/datas'
import { bindActionCreators } from 'redux';

class ClassListContainer extends Component {
  render() {
    const {datas, DataActions, currentPrice, budget} = this.props    

    return (
      <div>
        <ClassList datas={datas} DataActions={DataActions} currentPrice={currentPrice} budget={budget}/>
      </div>
    );
  }
}

export default connect(
  state =>({
    datas : state.datas.datas,
    currentPrice : state.datas.currentPrice,
    budget : state.datas.budget
  }),
  dispatch =>({
    DataActions : bindActionCreators(dataActions, dispatch)
  })
)(ClassListContainer)

