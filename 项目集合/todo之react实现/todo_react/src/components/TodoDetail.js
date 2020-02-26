import React, {Component} from 'react'
import TodoApi from '../api/todo'

class TodoDetail extends Component {
    constructor(props) {
        super(props)
        this.api = new TodoApi()
        this.state = {
            id: this.props.match.params.id,
            todo: {},
        }
    }

    componentDidMount() {
        let id = this.state.id
        let todoId = String(id)
        this.api.detail(todoId, (r) => {
            this.setState({
                todo: r,
            })
        })
    }

    timeToStandard(t) {
        let time = new Date(t)
        let day = time.getDate()
        let month = time.getMonth() + 1
        let year = time.getFullYear()
        let hour = time.getHours()
        let min = time.getMinutes()
        let sec = time.getSeconds()
        return `${year}/${month}/${day} ${hour}:${min}:${sec}`
    }

    render() {
        let todo = this.state.todo
        todo.updateTime = this.timeToStandard(todo.updateTime)
        todo.createdTime = this.timeToStandard(todo.createdTime)
        todo.done = todo.done ? '完成' : '待做'
        return (
            <div className='todo-detail-wrapper'>
                <div className='todo-detail-content'>
                    {
                        Object.entries(todo).map((e, index) => {
                            let [k, v] = e
                            return (
                                <pre key={index} className='todo-detail-item'>
                                    <span className='todo-key'>
                                        ({k}):
                                    </span><span className='todo-value'>
                                        {v}
                                    </span>
                                </pre>
                            )
                        })
                    }
                </div>
            </div>
        )
    }
}

export default TodoDetail