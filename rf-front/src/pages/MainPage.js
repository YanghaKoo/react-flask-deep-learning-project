import React, { Component } from 'react';
import './MainPage.scss'
import Footer from "components/common/Footer";
import ImageSubmitContainer from '../containers/ImageSubmitContainer';

class MainPage extends Component {  
   
  render() {
    return (
      <div>        
        <div className="main-page">
        <center>          
          <ImageSubmitContainer/>                    
        </center>      
        </div>
        <Footer/>  
      </div>
    );
  }
}

export default MainPage;