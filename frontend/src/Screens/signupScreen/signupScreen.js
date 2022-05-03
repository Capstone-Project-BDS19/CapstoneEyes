
import React, {useState} from 'react';
import SignupForm from '../../Components/Signupform/SignupForm';
import {useNavigate} from 'react-router-dom'
import axiosInstance from '../../axios';
import axios, { AxiosError } from 'axios';

export function SignUpScreen(){

  const history = useNavigate();
  const [user, setUser] = useState({username: "", email: "", password: ""});
  const [repeatPassword, setRepeatPassword] = useState("");
  const [error, setError] = useState("");
  
  const Signup = (details, repeatPassword) => {
      console.log(details.email);
      if ((details.email === '') || (details.username === '') || (details.password === '')){
        setError('Please fill in the required details')
      }
      else{
        if (details.password !== repeatPassword){
                console.log("unmatched password")
                setError("Unmatched password. Please try again!")
        } else if (details.password.length <8){
            setError("The password must contain at least 8 characters")
        } else {
                console.log("Matched password");
                axiosInstance
                    .post('user/create/', {
                        email: details.email,
                        user_name: details.username,
                        password: details.password,
                    }) 

                    .then((res) => {
                        history('/login')
                        console.log('Logged in')
                        console.log(res)
                        console.log(res.data)
                    }).catch((err) => {
                        console.log(err)
                        if (err.response.data.non_field_errors[0] === 'This email already exists'){
                            setError('This email already exists. Please try again!')
                        } else if (err.response.data.non_field_errors[0] === 'This username already exists'){
                            setError('This username already exists. Please try again!')
                        } else{
                            console.error(err)
                // }
            }})
    }}
  }

  return(
      <div className = "App">
          <SignupForm Signup={Signup} error = {error}/>    
      </div>
  )
}