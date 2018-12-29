import React, { Component } from "react";
import axios from "axios";
import "./ImageSubmit.scss";
import ReactLoading from "react-loading";
import {withRouter} from 'react-router-dom'

class ImageSubmit extends Component {
  state = {
    budget: "",
    file: "",
    imagePreviewUrl: "",
    loading: false
  };

  handleSubmit = async e => {
    e.preventDefault();
    const { budget } = this.state;
    const { setData, history } = this.props;
    
    if (!this.state.imagePreviewUrl) {
      alert("Please Upload Image.");
      return;
    }

    const { file } = this.state;
    const fd = new FormData();
    fd.append("image", file, file.name);    

    const contentType = {
      headers: { "Content-Type": "multipart/form-data" }
    };
    this.setState({
      loading: true
    });
    
    // back-end로 image 제출
    const allData = await axios.post("/", fd, contentType);

    this.setState({
      loading: false
    });

    setData({ data: allData.data, budget });    
    history.push("/select")
  };

  // image 미리보기
  handleImageChange = e => {
    e.preventDefault();
    let reader = new FileReader();
    let file = e.target.files[0];

    reader.onloadend = () => {
      this.setState({
        file: file,
        imagePreviewUrl: reader.result
      });
    };

    reader.readAsDataURL(file);
  };

  // 숫자만 입력 가능한 budget input
  handleBudget = e => {
    if (!isNaN(Number(e.target.value))) {
      this.setState({
        budget: e.target.value
      });
    }
  };

  render() {
    let { imagePreviewUrl } = this.state;
    let $imagePreview = null;
    if (imagePreviewUrl) {
      $imagePreview = <img src={imagePreviewUrl} />;
    }

    // 로딩중일 때 로딩컴포넌트
    if (this.state.loading) {
      return (
        <div className="loading">
          <ReactLoading type="bars" color="#8f8681" height={400} width={375} />
        </div>
      );
    }

    // 로딩중이 아닐 때 예산/이미지 제출 폼
    return (      
      <div className="previewComponent">
        <form>
          <div className="top">
          <input
            className="budget"
            placeholder="Insert Budget"
            onChange={this.handleBudget}
            value={this.state.budget}
          />          
          <input
            className="fileInput"
            type="file"            
            onChange={e => this.handleImageChange(e)}
          />
          </div>
          <div className="imgPreview">{$imagePreview}</div>
          <button
            className="submitButton"
            type="submit"
            onClick={e => this.handleSubmit(e)}
          >
            Upload Image
          </button>
        </form>
      </div>
    );
  }
}

export default withRouter(ImageSubmit)
