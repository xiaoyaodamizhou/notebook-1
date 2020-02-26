import React, { Component } from 'react'
import TodoApi from "../api/todo"
import {Link} from 'react-router-dom'

class TodoList extends Component {
    render() {
        let todos = this.props.todos
        return (
            <ul>
                {todos.map(t => (
                    <li key={t.id}>
                        <TodoItem todo={t} onUpdate={this.props.onUpdate} onDelete={this.props.onDelete}/>
                    </li>
                ))}
            </ul>
        )
    }
}

class TodoItem extends Component {
    constructor(props) {
        super(props)
        this.api = new TodoApi()
        let {task, id, done} = this.props.todo
        this.state = {
            editing: false,
            text: task,
            todo: {
                task,
                id,
                done,
            }
        }
    }

    onEdit = () => {
        this.setState({
            editing: true
        })
    }

    onDelete = () => {
        let {id} = this.state.todo
        let todoId = String(id)
        this.api.delete(todoId, (r) => {
            this.props.onDelete(id)
        })
    }

    updateTodo = (todoId, data) => {
        this.api.update(todoId, data, (r) => {
            this.setState({
                todo: r,
                editing: false,
            })
            // console.log('onupdate', this.props.onUpdate, this.props)
            this.props.onUpdate(this.state.todo)
        })
    }

    onSubmit = () => {
        let {id} = this.state.todo
        let text = this.state.text
        let todoId = String(id)
        let data = {
            task: text
        }
        this.updateTodo(todoId, data)
    }

    onCancel = () => {
        this.setState({
            editing: false,
        })
    }


    onChange = (e) => {
        this.setState({
            text: e.target.value,
        })
    }

    toggleComplete = () => {
        let {id, done} = this.state.todo
        let data = {
            done: !done,
        }
        let todoId = String(id)
        this.updateTodo(todoId, data)
    }

    render() {
        let {done} = this.state.todo
        let {id, task} = this.state.todo
        let todo = null
        if (this.state.editing) {
            todo = (
                <div>
                    <button onClick={this.onSubmit}>提交</button>
                    <button onClick={this.onCancel}>取消</button>
                    <input type="text" className='input-edit' value={this.state.text} onChange={this.onChange}/>
                </div>
            )
        } else {
            let text = this.state.todo.done ? '取消完成' : '标记完成'
            todo = (
                <div>
                    <button onClick={this.onEdit}>编辑</button>
                    <button onClick={this.onDelete}>删除</button>
                    <button onClick={this.toggleComplete}>{text}</button>
                    <Link to={`/todo/${id}`}>{task}</Link>
                </div>
            )
        }

        let cls = done ? 'todo-complete' : ''
        return (
            <div className={`todo-cell ${cls}`}>
                {todo}
            </div>
        )
    }
}

export default TodoList
