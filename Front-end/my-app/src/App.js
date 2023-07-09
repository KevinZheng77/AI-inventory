import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import NavBar from "./NavBar";
import About from './Pages/about'
import Signin from './Pages/Signin';
import Signup from './Pages/Signup';
import Home from './Pages/Home';

function App() {
  return (
    <>
    <NavBar />
      <div className="Website Container">
        <Routes>
          <Route path='/' element={<Home />}></Route>
          <Route path='/signin' element={<Signin />}></Route>
          <Route path='/signup' element={<Signup />}></Route>
          <Route path='/about' element={<About />}></Route>
        </Routes>
      </div>
    </>
  );
}

export default App;
