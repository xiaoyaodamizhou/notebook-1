const movie = require('../model/movie')

const all = {
    path: '/api/movie/all',
    method: 'get',
    func(request, response) {
        let ms = movie.all()
        let r = JSON.stringify(ms)
        response.send(r)
    }
}

const routes = [
    all,
]

module.exports.routes = routes


