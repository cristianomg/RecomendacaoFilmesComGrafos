import React from 'react';
import './App.css';
import logo from './assets/logo.png';


import Routes from './routes';

function App() {
  return (
    <div className="container">
      <img src={logo} alt="GrafosAnyWhere"/>
      <div className="content">
        <Routes />
      </div>
      <div className="footer">
      <strong>©2019 Grafos Anywhere. All Rights Reserved.</strong>
      </div>
    </div>
  );
}

export default App;
