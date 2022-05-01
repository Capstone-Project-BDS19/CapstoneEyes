
import React, {useState} from 'react';
import LoginForm from '../../Components/LoginForm/LoginForm';
import { useNavigate } from 'react-router-dom';
import axiosInstance from '../../axios'; 

export function LogInScreen(){
  const history = useNavigate();

  const [user, setUser] = useState({email: "", password:""})
  const [error, setError] = useState("");
  
  const Login = details => {
      console.log(details);

      axiosInstance
            .post('token/', {
                  email: details.email,
                  password: details.password
            })
            .then((res) => {
                  localStorage.setItem('access_token', res.data.access);
                  localStorage.setItem('refresh_token', res.data.refresh);
                  axiosInstance.defaults.headers['Authorization'] =
                      'JWT ' + localStorage.getItem('access_token');
                  history('/');
                  console.log('Logged in');
            })
     
      // else {
      //   console.log("Incorrect credentials. Please try again!")
      //   setError("Incorrect credentials. Please try again!")
      // }
  }

  const Logout = () => {
      console.log("Logout");
      setUser({ name: "", email: ""});
  }

  return(
      <div className = "App">
        <LoginForm Login = {Login} error = {error}/>    
      </div>
  )
}


