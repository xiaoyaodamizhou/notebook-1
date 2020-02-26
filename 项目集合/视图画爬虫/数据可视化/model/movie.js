const fs = require('fs')
const movieFilePath = 'db/movie.json'

const loadMovies = () => {
    let content = fs.readFileSync(movieFilePath, 'utf8')
    let ms = JSON.parse(content)
    return ms
}

const m = {
    data: loadMovies()
}

m.all = function() {
    let ms = this.data
    return ms
}

module.exports = m


