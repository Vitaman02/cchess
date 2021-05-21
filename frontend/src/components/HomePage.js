import React, { Component } from "react";
import { BrowserRouter as Router, Switch, Route, Link, Redirect, useParams } from "react-router-dom";
import Play from "./Play";
import Login from "./Login";
import Register from "./Register";
import Analysis from "./Analysis";
// import Profile from "./Profile";


export default class HomePage extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (<Router>
            <Switch>
                <Route exact path="/"></Route>
                <Route path="/play" component={Play}></Route>
                <Route path="/analysis" component={Analysis}></Route>
                <Route path="/register" component={Register}></Route>
                <Route path="/login" component={Login}></Route>
                <Route path="/profile/:username" children={<Profiler/>}></Route>
            </Switch>
        </Router>);
    }
}

function Profiler() {
    let {username} = useParams();
    return (
        <div>
            <h3>Username: {username}</h3>
        </div>
    )
}
