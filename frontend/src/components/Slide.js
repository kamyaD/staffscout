import React, { Component } from "react";


export default function Slide() {
        return ( 
    <>
    <div id="myCarousel" class="carousel slide carousel-fade" data-ride="carousel slide" style={{marginLeft:"-20rem" ,position:"relative"}}>
            <ol class="carousel-indicators">
                <li data-target="#myCarousel" data-slide-to="0" class="active"></li>
                <li data-target="#myCarousel" data-slide-to="1"></li>
                <li data-target="#myCarousel" data-slide-to="2"></li>
             </ol>
        
        <div class="carousel-inner" style={{borderRadius:"5px"}}>
            <div class="carousel-item active" style={{height:"32rem", marginLeft:"-17rem",marginTop:"7rem",color:"white",position:"relative",backgroundColor:"#000", borderRadius:"5px"}}>
                {/* <div class="container" style={{position: "absolute", bottom:"0", left:"6", right:"0", paddingBottom:"5px"}}> */}
                <img class="d-block w-100" src="static/images/slides/header1.jpg" alt="First slide" style={{position:"absolute",bottom:"0", left:"0", backgroundSize:"cover",opacity:"0.7",right:"0", top:"0", borderRadius:"5px"}}/>
                <div class="carousel-caption" style={{position: "absolute", bottom:"5", left:"-60rem", right:"0", paddingBottom:"5px"}}>
                <h3>Where talent meets opportunity</h3>
                <p>Dont wait</p>
                <a href="/signup" class="btn btn-lg btn-outline-warning">
                Sign up today
                </a>
                </div>
                {/* </div> */}
            </div>
            <div class="carousel-item " style={{height:"32rem",marginTop:"7rem",marginLeft:"-17rem", color:"white",position:"relative",backgroundColor:"#000", borderRadius:"5px"}}>
                {/* <div class="container" style={{position: "absolute", bottom:"0", left:"6", right:"0", paddingBottom:"5px"}}> */}
                <img class="d-block w-100" src="static/images/slides/header2.jpg" alt="First slide" style={{position:"absolute",bottom:"0", left:"0", backgroundSize:"cover",opacity:"0.7",right:"0", top:"0", borderRadius:"5px"}}/>
                <div class="carousel-caption" style={{position: "absolute", bottom:"5", left:"-60rem", right:"0", paddingBottom:"5px"}}>
                <h1>Career Advisory</h1>
                <p>get it now!</p>
                <a href="/signup" class="btn btn-lg btn-outline-warning">
                    Sign up today
                </a>
                </div>
            </div>
            <div class="carousel-item " style={{height:"32rem",marginTop:"7rem",marginLeft:"-17rem", color:"white",position:"relative",backgroundColor:"#000",borderRadius:"5px"}}>
                {/* <div class="container" > */}
                <img class="d-block w-100" src="static/images/slides/header3.jpg" alt="First slide" style={{position:"absolute",bottom:"0", left:"0", backgroundSize:"cover",opacity:"0.7",right:"0", top:"0", borderRadius:"5px"}}/>
                <div class="carousel-caption" style={{position: "absolute", bottom:"5", left:"-60rem", right:"0", paddingBottom:"5px"}}>
                <h1>Tons of opportunities</h1>
                <p>Join in!</p>
                <a href="/signup" class="btn btn-lg btn-outline-warning">
                    Sign up today
                </a>
                </div>
            </div>
            <a class="carousel-control-prev" href="#myCarousel" style={{marginTop:"7rem"}} role="button" data-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="sr-only"></span>
              </a>
            <a class="carousel-control-next" href="#myCarousel" style={{marginTop:"7rem"}}role="button" data-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="sr-only"></span>
           </a>
        </div>
    </div>
    
    </>
    )

}