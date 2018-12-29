import React, { Component } from 'react';
import CalculateBudget from '../components/select/CalculateBudget';
import { connect } from 'react-redux'

class CalculateBudgetContainer extends Component {
  render() {
    return (
      <div>
        <CalculateBudget budget={this.props.budget} currentPrice={this.props.currentPrice}/>
      </div>
    );
  }
}

export default connect(
  state => ({
    budget : state.datas.budget,
    currentPrice : state.datas.currentPrice
  })
)(CalculateBudgetContainer)