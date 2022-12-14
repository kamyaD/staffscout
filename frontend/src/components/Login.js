import React, { Component } from "react";
import Header from './Header';
import http from "../http-common";


// const getAll = () => {
//     return http.get("/candidate/");
//   };
export default class Login extends Component {
    state = {
        candidates:[]
    }
    constructor(props){
        super(props);
        http.get("/candidate/").then(res=>{
            console.log(res.data)
        })
    }

    render() {
        return (
        <div class="">
            <Header/>
            
            <div class="container" style={{marginTop: "15rem"}}>
                <div class="row">
                    <div class="col-4">
                    <form class="">
                        <div class="form-group">
                            <label for="exampleInputEmail1">Email address</label>
                            <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email" />
                            <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>
                        </div>
                        <div class="form-group">
                            <label for="exampleInputPassword1">Password</label>
                            <input type="password" class="form-control" id="exampleInputPassword1" placeholder="Password" />
                        </div>
                        {/* <div class="form-group form-check">
                            <input type="checkbox" class="form-check-input" id="exampleCheck1" />
                            <label class="form-check-label" for="exampleCheck1">Check me out</label>
                        </div> */}
                        <button type="submit" class="btn btn-outline-warning">Submit</button>
                    </form>
                    </div>
                    <div class="col-6">
                    <img class=""  src={"static/images/recruited.jpg"}  alt="Card image cap"/>

                    </div>
                </div>
            </div>
            
        </div>
        );
    }
}