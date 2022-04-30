
import React, {useState} from 'react';
import SignupForm from '../../Components/Signupform/SignupForm';


export function SignUpScreen(){
  const adminUser = {
      email: "admin@admin.com",
      password: "admin123"   
  }

  const [user, setUser] = useState({username: "", email: "", password: ""});
  const [repeatPassword, setRepeatPassword] = useState("");
  const [error, setError] = useState("");
  
  const Signup = (details, repeatPassword) => {
      console.log(details);

      if (details.password == repeatPassword){
          console.log("Matched password")
        //   console.log(details.password);
        //   console.log(repeatPassword)
          setUser({
              username: details.username,
              email: details.email,
              password: details.password
          })
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