import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import Listing  from './Listing';
import Slideshow from './Fade';
import CitiesSlider from './script';
import reportWebVitals from './reportWebVitals';
import DataModule from './SecondPage';
// import {
//   BrowserRouter as Router,
//   Switch,
//   Route,
//   Link
// } from "react-router-dom";
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'
// import { Routes ,Route } from 'react-router-dom';



const slides = [
  {
    city: '',
    country: 'Potico',
    img: 'https://raw.githubusercontent.com/prashant3167/fastrestbai/main/static/restbai_test/323570__000.jpg',
  },
  {
    city: 'Interior',
    img: 'https://raw.githubusercontent.com/prashant3167/fastrestbai/main/static/restbai_test/323570__003.jpg',
  },
  {
    city: 'Kitchen',
    img: 'https://raw.githubusercontent.com/prashant3167/fastrestbai/main/static/restbai_test/323570__009.jpg',
  }
];


ReactDOM.render(
  <React.StrictMode>
    {/* <Router> */}
    <Router>
    <Routes>
    <Route path='/info/:id' element={<DataModule/>} />
    <Route path='/' element={<App/>} />
    </Routes>
    </Router>

      {/* <Switch>
      <Route path="/info/">
          <h1>test</h1>
        </Route>
        <Route path="/">
          <App />
        </Route>
      </Switch>
    </Router> */}
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
