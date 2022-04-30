import React, {useState} from 'react';
import {Link} from 'react-router-dom'
import "./LoginForm.css"
import * as AiIcons from "react-icons/ai"


function LoginForm({Login, error}){
    const [details, setDetails] = useState({username: "", password: "", password:""});
    const [passwordShown, setPasswordShown] = useState(false);

    const submitHandler = e => {
        e.preventDefault() //prevent re-render

        Login(details);
    }

    const togglePassword =() =>{
        setPasswordShown(!passwordShown)
    }

    
    return (
        <form onSubmit = {submitHandler}>
            <div className = "form-inner">
                <h2> Login to continue </h2>
                <div className = "form-group">
                    <input type="text" name= "username" id= "username" 
                    onChange = {e => setDetails({...details, username: e.target.value})} 
                    value = {details.name}
                    placeholder = "Username/ Email"></input>
                </div>
                <div className = "form-group-pwd">
                    <input type= {passwordShown ? "text" : "password"} 
                    name= "password" id= "password"
                    onChange = {e => setDetails({...details, password: e.target.value})}
                    value = {details.password}
                    placeholder = "Password"
                    className = "input-pwd"></input>
                    <AiIcons.AiOutlineEye className = "pwd-button" onClick = {togglePassword} />
                </div>

                <div className = "form-group">
                    <div className='forgot-pwd'>
                        <Link to=  "/"> Forgot Password? </Link>
                    </div>
                </div>
                <div className = "form-group-center">
                {(error != "") ? (<div className = "error">{error}</div>) :  ""}
                </div>
               <div className = "form-group-center"> 
                    <input type= "submit" value = "Login"/>
                </div>
                
                <div className = "form-group-center">
                    <p> Don't have an account? </p>
                    <Link to = "/signup"> Register now </Link>
                </div>
            </div>
        </form>
    )
}

export default LoginForm;