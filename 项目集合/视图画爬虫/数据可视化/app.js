const express = require('express')
const bodyParser = require('body-parser')

const app = express()

app.use(bodyParser.json())
app.use(express.static('static'))

const log = console.log.bind(console)


const registerRoutes = function (app, routes) {
    // log('routes', routes)
    for (let i = 0; i < routes.length; i++) {
        let route = routes[i]
        // log('route', i, route)
        app[route.method](route.path, route.func)
    }
}

const routeIndex = require('./route/index')
const routeMovie = require('./route/movie')

registerRoutes(app, routeIndex.routes)
registerRoutes(app, routeMovie.routes)

const main = () => {
    let host = 'localhost'
    let port = 8000
    let server = app.listen(port, host, function() {
        // let address = server.address().address
        // let port = server.address().port
        console.log(`访问地址 http://${host}:${port}`)
    })
}

if (require.main === module) {
    main()
}
