import React, {useState} from 'react';
import {Link} from 'react-router-dom'
import "./LoginForm.css"
import * as AiIcons from "react-icons/ai";
import {useNavigate} from 'react-router-dom';


function LoginForm({Login, error}){
    const history = useNavigate();
    const initialFormData = Object.freeze({
        email: '',
        password:'',
    })

    const [details, setDetails] = useState(initialFormData)
    const [passwordShown, setPasswordShown] = useState(false);

    const handleChange = e => {
        setDetails({
            ...details,
            [e.target.name] : e.target.value.trim(),
        })
    }

    const handleSubmit = e => {
        e.preventDefault() //prevent re-render
        console.log(details)
        Login(details);
    }

    const togglePassword =() =>{
        setPasswordShown(!passwordShown)
    }

    
    return (
        <form>
            <div className = "form-inner">
                <h2> Login to continue </h2>
                <div className = "form-group">
                    <input type="text" name= "email" id= "email" 
                    onChange = {handleChange}
                    value = {details.name}
                    placeholder = "Email"></input>
                </div>
                <div className = "form-group-pwd">
                    <input type= {passwordShown ? "text" : "password"} 
                    name= "password" id= "password"
                    onChange = {handleChange}
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
                    <input type= "submit" value = "Login"
                    onClick = {handleSubmit}/>
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