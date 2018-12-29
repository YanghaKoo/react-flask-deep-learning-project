import React, { Component } from 'react';
import ImageSubmit from '../components/main/ImageSubmit/ImageSubmit';
import { connect } from 'react-redux'
import * as dataActions from 'store/modules/datas'
import { bindActionCreators } from 'redux';

class ImageSubmitContainer extends Component {
  render() {
    const {DataActions} = this.props
    return (
      <div>
        <ImageSubmit setData={DataActions.setData}/>
      </div>
    );
  }
}

export default connect(
  null,
  dispatch => ({
    DataActions : bindActionCreators(dataActions, dispatch)
  })
)(ImageSubmitContainer)