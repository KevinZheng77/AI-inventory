import React from "react";
import { Link, useLocation } from "react-router-dom";
import { useGlobalContext } from "../context/Globalcontext";

const Header = () =>{
    const {logoutfunction} = useGlobalContext();
    const { pathname } = useLocation();
    const handleLogout = () => {
        logoutfunction();
      };
    return(
        <div className="main-header">
            <div className="main-header_inner">
                <div className="main-header_left">
                    <Link to="/">Inventory</Link>
                </div>
                <div className="main-header_right">
                <button className="btn" onClick={handleLogout}>Logout</button>
                </div>
            </div>
        </div>
    )
}

export default Header;