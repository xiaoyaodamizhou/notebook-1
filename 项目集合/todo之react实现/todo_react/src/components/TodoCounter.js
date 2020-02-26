import React, {Component} from 'react'
import './todoCounter.css'


class TodoCounter extends Component {
    render() {
        let todos = this.props.todos
        let total = todos.length
        let completeLength = todos.filter(e => e.done).length
        let uncompleteLength = todos.filter(e => !e.done).length
        return (
            <div className="todo-counter">
                <div className='todo-counter-sum'>统计:</div>
                <div className='todo-table'>
                    <div className='todo-row'>
                        <span className="cell">总计</span>
                        <span className="cell">完成</span>
                        <span className="cell">未完成</span>
                    </div>
                    <div className='todo-row'>
                        <span className="cell">{total}</span>
                        <span className="cell">{completeLength}</span>
                        <span className="cell">{uncompleteLength}</span>
                    </div>
                </div>
            </div>
        )
    }
}

export default TodoCounter