
import React, {useState} from 'react';
import {LogInScreen} from './Screens/loginScreen/loginScreen';
import {SignUpScreen} from './Screens/signupScreen/signupScreen';
import {NavBar} from './Components/NavBar/NavBar';
//import {ModelStreaming} from './Components/ModelStreaming/modelStreaming';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import {About} from "./Components/AboutUs/About";
import { Home } from './Components/Home/Home';
import { Portfolio } from './Components/Portfolio/Portfolio';
import { Contact } from './Components/ContactUs/Contact';

export default function App(){
  return(
      <Router>
        <NavBar/>
        <Routes>
          <Route path = "/" caseSensitive={false} element= {<Home/>} />
          <Route path = "/login" caseSensitive={false} element = {<LogInScreen/>} />
          <Route path = "/signup" caseSensitive={false} element = {<SignUpScreen/>} />
          {/* <Route path = '/modelStreaming' caseSensitive={false} element = {<ModelStreaming/>} /> */}
          <Route path = "/aboutus" caseSensitive={false} element= {<About/>} />
          <Route path = "/portfolio" caseSensitive={false} element= {<Portfolio/>} />
          <Route path = "/contact" caseSensitive={false} element= {<Contact/>} />
        </Routes>
      </Router>
  )
}