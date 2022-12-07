import React, { Component } from "react";
import Header from './Header';
import Slide from './Slide';
import Card from './Card';



export default function HomPage() {
        return (
            <div class="container">
                <Header/>
                <Slide/>
            <div class="container" tyle={{width:"100%"}}>
            <div class="row gy-4" style={{width:"100%"}}>
                <div class="col-sm">
                <Card 
                image={"static/images/slides/jobs.png"} 
                title={"Looking For a Job"} 
                body={"Some quick example text to build on the card title and make up the bulk of the card's content."
                 }/>
                </div>
                <div class="col-sm">
                <Card 
                image={"static/images/slides/Professional.png"}
                title={"Card title2"} 
                body={"Some quick example text to build on the card title and make up the bulk of the card's content."
                 }/>
                </div>
                <div class="col-sm" >
                <Card 
                image={"static/images/slides/Semi-skilled.png"}
                title={"Card title3"} 
                body={"Some quick example text to build on the card title and make up the bulk of the card's content."
                }/>
                </div>
                
            </div>
            </div>
                
                
            </div>
        )
    }
