
import React, {useState} from 'react';
import LoginForm from '../../Components/LoginForm/LoginForm';

export function LogInScreen(){
  const adminUser = {
      username: "admin@admin.com",
      password: "admin123"   
  }

  const [user, setUser] = useState({username: "", password:""})
  const [error, setError] = useState("");
  
  const Login = details => {
      console.log(details);

      if (details.username == adminUser.username && details.password == adminUser.password){
        console.log("Logged in");
        setUser({
          username: details.username,
          password: details.password
        })
      } else {
        console.log("Incorrect credentials. Please try again!")
        setError("Incorrect credentials. Please try again!")
      }
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


