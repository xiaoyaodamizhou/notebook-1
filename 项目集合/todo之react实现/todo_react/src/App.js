import React, {Component} from 'react'
import {BrowserRouter as Router, Route} from 'react-router-dom'

import Todo from './components/todo'
import TodoDetail from './components/TodoDetail'
import './App.css'

class App extends Component {
    render() {
        return (
            <Router>
                <div className="todo-box">
                    <Route exact path="/" component={Todo}/>
                    <Route exact path="/todo" component={Todo}/>
                    <Route exact path="/todo/:id" component={TodoDetail}/>
                </div>
            </Router>
        )
    }
}

export default App