import React from "react";
import { Switch, Route } from "react-router-dom";
import { MainPage, SelectPage, NotFound } from "pages";
import Navbar from "./components/common/Navbar/Navbar";
import "./App.js";

const App = () => {
  return (
    <div className="app">
      <Navbar />
      <Switch>
        <Route exact path="/" component={MainPage} />
        <Route path="/select" component={SelectPage} />
        <Route component={NotFound}/>
      </Switch>
    </div>
  );
};

export default App;
