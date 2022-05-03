import React, {useState} from 'react';
import "./Signup.css"
import * as AiIcons from "react-icons/ai"
import axiosInstance from '../../axios';


function SignupForm({Signup, error}){

    const initialFormData = Object.freeze({
        email: '',
        username: '',
        password:'',
    })

    //const [details, setDetails] = useState({username: "", email: "", password: ""});
    const [details, setDetails] = useState(initialFormData)
    const [repeatPassword, setRepeatPassword] = useState("");
    const [passwordShown1, setPasswordShown1] = useState(false);
    const [passwordShown2, setPasswordShown2] = useState(false)

    const handleChange = (e) =>{
        setDetails({
            ...details,
            //trimming whitespace
            [e.target.name]: e.target.value.trim(),
        })
    }
    
    const submitHandler = e => {
        e.preventDefault();
        console.log(details)
        Signup(details, repeatPassword)
    }

    const togglePassword1 =() =>{
        setPasswordShown1(!passwordShown1)
    }

    const togglePassword2 =() =>{
        setPasswordShown2(!passwordShown2)
    }

    return(
        <form onSubmit = {submitHandler}>
            <div className= "form-inner">
                <h2> Create an account </h2>
                <div className = "form-group">
                    <input type="email" name= "email" id ="email"
                    //onChange = {e => setDetails({...details, email: e.target.value})}
                    onChange = {handleChange}
                    placeholder="Email*"> 
                    </input>
                </div>
                <div className = "form-group">
                    <input type="text" name="username" id = "username"
                    //onChange = {e => setDetails({...details, username: e.target.value})}
                    onChange = {handleChange}
                    placeholder = "Username*"></input>
                </div>
            
                <div className = "form-group-pwd">
                    <input type= {passwordShown1 ? "text" : "password"}  name="password" id = "password"
                    //onChange = {e => {setDetails({...details, password: e.target.value})}}
                    onChange={handleChange}
                    placeholder = "Password*"
                    className = "input-pwd">
                    </input>
                    <AiIcons.AiOutlineEye className = "pwd-button" onClick = {togglePassword1} />
                </div>
                <div className = "form-group-pwd">
                    <input type= {passwordShown2 ? "text" : "password"} 
                    placeholder = "Repeat Password*"
                    className = "input-pwd"
                    onChange = {e => {setRepeatPassword(e.target.value)}}>
                    </input>
                    <AiIcons.AiOutlineEye className = "pwd-button" onClick = {togglePassword2} />
                </div>
                <div className = "form-group-center">
                {(error != "") ? (<div className = "error"> {error} </div>): ""}
                </div>
                <div className = "form-group-center">
                    <input type = "submit" value = "Create your account"/>
                </div>
            </div>
        </form>
    
        )
}

export default SignupForm;