import React, { Component } from 'react';
import "./Original.scss"
import {connect} from 'react-redux'


class Original extends Component {
  render() {
    const { label, id, now } = this.props
    const src = "/static/output/"+ now + "." + id + ".jpg"
    return (
      <div className="original">        
        <img src={src} width="250px" height="250px"/>        
        <h2>{label}</h2>
      </div>
    );
  }
}

export default connect(
  state => ({
    now : state.datas.id
  })
)(Original)