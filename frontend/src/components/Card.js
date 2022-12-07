import React, { Component } from "react";


export default function Card(props) {
    return (
        <div class="container-fluid">
            
            <div class="card h-100" style={{width: "25rem", marginLeft:"-19rem", marginTop:"2rem",position:"relative", backgroundColor:"whitesmoke"}}>
                <img class="card-img-top" src={props.image} alt="Card image cap" style={{height:"5%"}}/>
                <div class="carousel-caption" style={{position: "absolute", bottom:"5", left:"-60rem", right:"0", paddingBottom:"5px"}}>
                <h5>Tons of opportunities</h5>
                <p>Join in!</p>
                <a href="" class="btn btn-lg btn-outline-warning">
                    Sign up today
                </a>
                </div>
                {/* <div class="card-body">
                    <h5 class="card-title text-warning">{props.title}</h5>
                    <p class="card-text">{props.body}</p>
                    <a href="#" class="btn btn-outline-warning">Go somewhere</a>
                </div> */}
                </div>
        </div>
    )
}