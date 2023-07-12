import React from "react";
import axios from "axios";
import { useGlobalContext } from "../context/Globalcontext";

const SignupForm = () => {
    const {getCurrentUser} = useGlobalContext();
    const [email, setEmail] = React.useState("");
    const [password, setPassword] = React.useState("");
    const [name, setName] = React.useState("");
    const [confirmPassword, setConfirmPassword] = React.useState("");
    const [errors, setErrors] = React.useState({});

    const onSubmit = (e) =>{
        e.preventDefault();
        let data = {};
        data = {
            name,
            email,
            password,
            confirmPassword,
        };
        //API call
        axios.post("/api/auth/register", data).then(() =>{
            getCurrentUser();
        }).catch(errors =>{
            if(errors?.response?.data){
                setErrors(errors.response.data)
            }
        })
    }
    return(
        <div className="auth">
            <div className="auth_box">
                <div className="auth_header">
                    <h1>Register</h1>
                </div>
                <form onSubmit={onSubmit}>
                    <div className="auth_field">
                        <label>Name</label>
                        <input type="text" value={name} 
                            onChange={(e) => setName(e.target.value)}/>
                    {errors.name &&(<p className="auth_error">{errors.name}</p>)}
                    </div>
                    <div className="auth_field">
                        <label>Email</label>
                        <input type="text" value={email}
                            onChange={(e) => setEmail(e.target.value)}/>
                        {errors.email &&(<p className="auth_error">{errors.email}</p>)}
                    </div>
                    <div className="auth_field">
                        <label>Password</label>
                        <input type="text" value={password} 
                            onChange={(e) => setPassword(e.target.value)}
                        />
                        {errors.password &&(<p className="auth_error">{errors.password}</p>)}
                    </div>
                    <div className="auth_field">
                        <label>Confirm Password</label>
                        <input type="text" value={confirmPassword} 
                            onChange={(e) => setConfirmPassword(e.target.value)}/>
                        {errors.confirmPassword &&(<p className="auth_error">{errors.confirmPassword}</p>)}
                    </div>
                    <div className="auth_footer">
                    {Object.keys(errors).length > 0 &&(
                        <p className="auth_error">Registration failed</p>
                    )}
                        <button className="btn">Register</button>
                    </div>
                </form>
            </div>
        </div>
    )
}

export default SignupForm;