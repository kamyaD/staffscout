import React, { Component } from "react";
// import { render } from "react-dom";
import Link,{BrowserRouter as Router,
    Routes, 
    Route, 
    Redirect
} from "react-router-dom";
import HomePage from "./HomePage";
import Login from "./Login";
import SignUp from "./SignUp";


function App() {
    return (
      <div className="container mw-100">
        <Routes>
          <Route path="/" element={ <HomePage/> } />
          <Route exact path="/login" element={<Login />} />
          <Route exact path="/signup" element={ <SignUp/> } />
        </Routes>
      </div>
    )
  }
  
  export default App
  

