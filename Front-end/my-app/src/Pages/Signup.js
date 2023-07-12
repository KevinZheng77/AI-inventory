import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Header from "./Header";
import '../main.scss';
import SignupForm from "./SignupForm";
const Signup = () => {
    return(
        <div>
            <SignupForm/>
        </div>
    )
}

export default Signup;