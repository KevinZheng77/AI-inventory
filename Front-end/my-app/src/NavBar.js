import React from "react";
import about from './Pages/about';
import Signup from './Pages/Signup';
import './styles.css';
import { Link, useMatch, useResolvedPath} from "react-router-dom";
export default function NavBar(){
    return(
        <nav className="LandingPageNavBar">
            <Link to='/' className="SiteTitle">AI Inventory</Link>
            <ul>
               <CustomLink to='/about'>About</CustomLink>
               <CustomLink to='/Signin'>Signin</CustomLink>
               <CustomLink to='/Signup'>Signup</CustomLink>
            </ul>
        </nav>
    );
}

function CustomLink({to,children, ...props}){
    const ResolvedPath = useResolvedPath(to)
    const isActive = useMatch({ path: ResolvedPath.pathname, end: true})
    return (
        <li className={isActive ? 'active' : ''}>
            <Link to={to} {...props}>{children}</Link>
        </li>
    )
}




