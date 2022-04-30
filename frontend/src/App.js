
import React, {useState} from 'react';
import {LogInScreen} from './Screens/loginScreen/loginScreen';
import {SignUpScreen} from './Screens/signupScreen/signupScreen';
import {NavBar} from './Components/NavBar/NavBar';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

export default function App(){
  return(
      <Router>
        <NavBar/>
        <Routes>
          <Route path = "/" caseSensitive={false} element = {<LogInScreen/>} />
          <Route path = "/signup" caseSensitive={false} element = {<SignUpScreen/>} />
          {/* <Route path = "/aboutus" caseSensitive={false} element = {<AboutUs/>} />
          <Route path = "/contactus" caseSensitive={false} element = {<ContactUs/>} /> */}
        </Routes>
      </Router>
  )
}