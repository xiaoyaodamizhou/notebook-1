const fs = require('fs')
const express = require('express')
const bodyParser = require('body-parser')
const cors = require('cors')

const app = express()
const log = console.log.bind(console)

app.use(express.static('static'))
app.use(bodyParser.json())
app.use(cors())

const loadTodos = () => {
    let data = fs.readFileSync('todo.json')
    let todos = JSON.parse(data)
    return todos
}

const saveTodos = (todos) => {
    let s = JSON.stringify(todos, null, 2)
    fs.writeFileSync('todo.json', s)
}

const todoList = loadTodos()

const sendHtml = (path, response) => {
    let options = {
        encoding: 'utf-8'
    }
    fs.readFile(path, options, (error, data) => {
        response.send(data)
    })
}

const sendJson = (data, response) => {
    let r = JSON.stringify(data, null, 2)
    response.send(r)
}

const abort = (response, code) => {
    let mapper = {
        400: 'Bad Request',
        404: 'Not Found',
    }
    let text = mapper[code]
    response.status(code).send(text)
}

const todoAdd = (form) => {
    if (todoList.length === 0) {
        form.id = 1
    } else {
        let tail = todoList[todoList.length - 1]
        form.id = tail.id + 1
    }
    let now = Date.now()
    form.createdTime = now
    form.updateTime = now
    form.done = false
    todoList.push(form)
    saveTodos(todoList)
    return form
}

const todoUpdate = (id, form) => {
    id = Number(id)
    let todo = todoList.find(e => e.id === id)
    if (todo === undefined) {
        return {}
    } else {
        todo.updateTime = Date.now()
        Object.entries(form).forEach(entry => {
            let [k, v] = entry
            todo[k] = v
        })
        saveTodos(todoList)
        return todo
    }
}

const todoDelete = (id) => {
    id = Number(id)
    let index = todoList.findIndex(e => e.id === id)
    if (index > -1) {
        let t = todoList.splice(index, 1)[0]
        return t
    } else {
        return {}
    }
}

app.get('/', (request, response) => {
    let path = 'index.html'
    sendHtml(path, response)
})

app.get('/api/todo/all', (request, response) => {
    sendJson(todoList, response)
})

app.post('/api/todo/add', (request, response) => {
    let form = request.body
    let todo = todoAdd(form)
    sendJson(todo, response)
})

app.post('/api/todo/update/:id', (request, response) => {
    let id = request.params.id
    let form = request.body
    let todo = todoUpdate(id, form)
    sendJson(todo, response)
})

app.get('/api/todo/delete/:id', (request, response) => {
    let id = request.params.id
    let todo = todoDelete(id)
    sendJson(todo, response)
})

const todoFetch = id => {
    id = Number(id)
    let todo = todoList.find(e => e.id === id)
    if (todo === undefined) {
        return {}
    } else {
        return todo
    }
}

app.get('/api/todo/:id', (request, response) => {
    let id = request.params.id
    let todo = todoFetch(id)
    sendJson(todo, response)
})

const main = () => {
    let host = 'localhost'
    let server = app.listen(8000, host, () => {
        // let host = server.address().address
        let port = server.address().port
        log(`访问地址: http://${host}:${port}`)
    })
}

if (require.main === module) {
    main()
}
