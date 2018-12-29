import React, { Component } from "react";
import ClassListItem from "components/select/ClassListItem";
import "./ClassList.scss";

class ClassList extends Component {
  
  // 추천된 set의 현재 값을 알기위해 여기서 current Price를 계산 후 redux level state에 저장
  componentDidMount() {
    const { datas, DataActions } = this.props;
    
    let recommendedPrice = 0;    
    datas.map(item => {
      item.sresult.map(item => {
        if (item.is_check === 1) {
          recommendedPrice += item.price;
        }
      });
    });
    DataActions.setPrice(recommendedPrice);
  }

  
  render() {
    const { datas } = this.props;
    if (!datas[0]){
      return (<div className="error">No Result or You Did Not Upload Proper Image</div>)
    }

    const items = datas.map(item => {
      return (
        <ClassListItem
          id={item.idx}
          key={item.idx}
          label={item.label}
          sresult={item.sresult}
        />
      );
    });

    return (
      <center>
        <div className="class-list">{items}</div>
      </center>
    );
  }
}

export default ClassList;
