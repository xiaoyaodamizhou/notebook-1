const fs = require('fs')

const sendHtml = function(path, response) {
    let options = {
        encoding: 'utf-8'
    }
    path = 'template/' + path
    fs.readFile(path, options, (err, data) => {
        response.send(data)
    })
}

const index = {
    path: '/',
    method: 'get',
    func: function(request, response) {
        let path = 'movie_index.html'
        sendHtml(path, response)
    }
}


const routes = [
    index,
]

module.exports.routes = routes