import React from "react";
import axios from "axios";
import { useGlobalContext } from "../context/Globalcontext";
import{Link, useNavigate} from "react-router-dom";

const SigninForm = () => {
    const navigate = useNavigate();
    const {getCurrentUser, user} = useGlobalContext();
    const [email, setEmail] = React.useState("");
    const [password, setPassword] = React.useState("");
    const [errors, setErrors] = React.useState({});

    React.useEffect(() =>{
        if(user && navigate ){
            navigate("/dashboard");
        }
    }, [user && navigate]);
    //submitting login
    const onSubmit = (e) =>{
        e.preventDefault();
        let data = {};
        data = {
            email,
            password,
        };
        //API call
        axios.post("/api/auth/login", data).then(() =>{
            getCurrentUser();
        }).catch(errors =>{
            if(errors?.response?.data){
                setErrors(errors.response.data)
            }
        })
    }
    return(
        <div className="signin-container">  
            <div className="auth">
                <div className="auth_box">
                    <div className="auth_header">
                        <h1>Login</h1>
                    </div>
                    <form onSubmit={onSubmit}>
                        <div className="auth_field">
                            <label>Email</label>
                            <input type="text" value={email}
                                onChange={(e) => setEmail(e.target.value)}
                            />
                        </div>
                        <div className="auth_field">
                            <label>Password</label>
                            <input type="text" value={password} 
                                onChange={(e) => setPassword(e.target.value)}/>
                        </div>
                        <div className="auth_footer">
                        {Object.keys(errors).length > 0 &&(
                            <p className="auth_error">{errors.errors}</p>
                        )}
                            <button className="btn">Login</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    )
}

export default SigninForm;