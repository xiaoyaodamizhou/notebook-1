import React, {Component} from 'react'
import TodoList from './TodoList'
import TodoCounter from './TodoCounter'
import TodoApi from '../api/todo'

import './todo.css'


class Todo extends Component {
    constructor(props) {
        super(props)
        this.api = new TodoApi()
        this.state = {
            todos: [],
            text: '',
        }
    }

    componentDidMount() {
        this.api.all(r => {
            this.setState({
                todos: r
            })
        })
    }

    onUpdate = (todo) => {
        let todos = this.state.todos
        let t = todos.find(e => e.id === todo.id)
        t.done = todo.done
        this.setState({
            todos: todos,
        })
    }

    onDelete = (id) => {
        let todos = this.state.todos
        let index = todos.findIndex(e => e.id === id)
        todos.splice(index, 1)
        this.setState({
            todos: todos,
        })
    }

    onChange = (e) => {
        this.setState({
            text: e.target.value,
        })
    }

    onSubmit = (e) => {
        e.preventDefault()
        if (this.state.text.length === 0) {
            return
        }
        let task = this.state.text
        let data = {
            task,
        }
        let todos = this.state.todos
        this.api.add(data, (r) => {
            todos.push(r)
            this.setState({
                todos: todos,
                text: '',
            })
        })
    }

    render() {
        let todos = this.state.todos
        return (
            <div className='todo-box-wrapper'>
                <h3 className='h-todo-header'>TODO</h3>
                <form onSubmit={this.onSubmit} className='todo-form'>
                    <label htmlFor="new-todo" className='todo-input-label'>
                        输入事项:
                    </label>
                    <input id="new-todo" onChange={this.onChange} value={this.state.text}/>
                    <button className='todo-button-submit'>
                        添加第 {todos.length + 1} 个 todo
                    </button>
                </form>
                <TodoCounter todos={todos}/>
                <TodoList todos={todos} onUpdate={this.onUpdate} onDelete={this.onDelete}/>
            </div>
        )
    }
}

export default Todo
