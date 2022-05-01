
import React, {useState} from 'react';
import SignupForm from '../../Components/Signupform/SignupForm';
import {useNavigate} from 'react-router-dom'
import axiosInstance from '../../axios';

export function SignUpScreen(){

  const history = useNavigate();
  const [user, setUser] = useState({username: "", email: "", password: ""});
  const [repeatPassword, setRepeatPassword] = useState("");
  const [error, setError] = useState("");
  
  const Signup = (details, repeatPassword) => {
      console.log(details);

      if (details.password == repeatPassword){
          console.log("Matched password");
          axiosInstance
                    .post('user/create/', {
                        email: details.email,
                        user_name: details.username,
                        password: details.password,
                    })
                    .then((res) => {
                        history('/login');
                        console.log(res)
                        console.log(res.data)
                    })
        //   setUser({
        //       username: details.username,
        //       email: details.email,
        //       password: details.password
        //   })
      } else {
          console.log("unmatched password")
          setError("Unmatched password. Please try again!")
      }
  }

  return(
      <div className = "App">
          <SignupForm Signup={Signup} error = {error}/>    
      </div>
  )
}