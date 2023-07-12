import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Header from "./Header";
import '../main.scss';
import SigninForm from "./SigninForm";

const Signup = () => {
    return(
        <div>
            <SigninForm/>
        </div>
    )
}

export default Signup;