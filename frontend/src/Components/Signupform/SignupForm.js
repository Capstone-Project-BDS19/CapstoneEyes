import React, {useState} from 'react';
import "./Signup.css"
import * as AiIcons from "react-icons/ai"


function SignupForm({Signup, error}){

    const [details, setDetails] = useState({username: "", email: "", password: ""});
    const [repeatPassword, setRepeatPassword] = useState("");
    const [passwordShown, setPasswordShown] = useState(false);


    const submitHandler = e => {
        e.preventDefault()
        Signup(details, repeatPassword)
    }

    const togglePassword =() =>{
        setPasswordShown(!passwordShown)
    }

    return(
        <form onSubmit = {submitHandler}>
            <div className= "form-inner">
                <h2> Create an account </h2>
                <div className = "form-group">
                    <input type="text" name="username" id = "username"
                    onChange = {e => setDetails({...details, username: e.target.value})}
                    placeholder = "Username"></input>
                </div>
                {/* <div className = "form-group">
                    <input type="email" name= "email" id ="email"
                    onChange = {e => setDetails({...details, email: e.target.value})}
                    placeholder="Email"> 
                    </input>
                </div> */}
                <div className = "form-group-pwd">
                    <input type= {passwordShown ? "text" : "password"}  name="password" id = "password"
                    onChange = {e => {setDetails({...details, password: e.target.value})}}
                    placeholder = "Password"
                    className = "input-pwd">
                    </input>
                    <AiIcons.AiOutlineEye className = "pwd-button" onClick = {togglePassword} />
                </div>
                <div className = "form-group-pwd">
                    <input type= {passwordShown ? "text" : "password"} 
                    placeholder = "Repeat Password"
                    className = "input-pwd"
                    onChange = {e => {setRepeatPassword(e.target.value)}}>
                    </input>
                    <AiIcons.AiOutlineEye className = "pwd-button" onClick = {togglePassword} />
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