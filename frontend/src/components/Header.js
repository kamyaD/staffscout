import React, { Component } from "react";


export default function Header() {
        return ( 
        <div class="container-fluid bg-light">
          <header id="header" class="header fixed-top d-flex align-items-center" style={{height: "100px", }}>
          <div class="block flex-initial mr-6 ">
            <div class="block flex-initial mr-6">
            {/* <i class="bi bi-list toggle-sidebar-btn" style={{height: "4rem", foat:"left"}}></i> */}
          </div>
            <div class="flex-initial mr-auto">
              <div class="flex items-center flex-shrink-0 text-white mr-6" >
                  <img src="static/images/logo.png" alt="" style={{height: "4rem", marginLeft:"100px", foat:"left"}}/>
              </div>
            </div>
        </div>
        

        <nav class="navbar navbar-expand-lg navbar-light bg-light" style={{marginLeft:"700px"}}>
        {/* <a class="navbar-brand" href="#">Navbar</a> */}
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
            <li class="btn btn-outline-warning">
                <a class="nav-link" href="#">Career Advisory</a>
            </li>
            <li class="btn btn-outline-warning">
                <a class="nav-link" href="#">CV Services</a>
            </li>
            <li class="btn btn-outline-warning">
                <a class="nav-link" href="#">Find a Job</a>
            </li>
            <li class="btn btn-outline-warning">
                <a class="nav-link "  href="#">Employers</a> 
            </li>
            <li class="btn btn-outline-warning">
                <a class="nav-link "  href="/login">Login</a> 
            </li>
            <li class="btn btn-outline-warning">
                <a class="nav-link "  href="/signup">SignUp</a> 
            </li>

            </ul>
        </div>
        </nav>
      </header>
      <div>
      
      </div>
      </div>


    )
    }