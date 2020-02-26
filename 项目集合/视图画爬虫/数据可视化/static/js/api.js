const log = console.log.bind(console)

const api = {}

api.ajax = (url, method, form, response) => {
    let request = {
        url,
        type: method,
        contentType: 'application/json',
        success: r => response(r)
    }

    if (method === 'post') {
        let data = JSON.stringify(form)
        request.data = data
    }

    $.ajax(request)
}

api.get = (url, response) => {
    let method = 'get'
    let request = {
        url,
        type: method,
        contentType: 'application/json',
        success(r) {
            response(r)
        }
    }
    $.ajax(request)
}

api.fetchMovies = function(success) {
    let url = '/api/movie/all'
    this.get(url, success)
}