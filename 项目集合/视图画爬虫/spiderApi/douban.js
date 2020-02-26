const fs = require('fs')
const request = require('syncrequest')
const cheerio = require('cheerio')

const log = console.log.bind(console)
const e = (selector) => {
    return document.querySelector(selector)
}

class Movie {
    constructor() {
        this.name = ''
        this.score = 0
        this.quote = ''
        this.ranking = 0
        this.coverUrl = ''
    }
}

const movieFromDiv = (div) => {
    let e = cheerio.load(div)
    let movie = new Movie()
    movie.name = e('.title').text()
    movie.score = e('.rating_num').text()
    movie.quote = e('.ing').text()
    let pic = e('.pic')
    movie.ranking = pic.find('em').text()
    movie.coverUrl = pic.find('img').attr('src')
    return movie
}

const ensurePath = (path) => {
    if (!fs.existsSync(path)) {
        fs.mkdirSync(path)
    }
}

const {cookie, userAgent} = require('./config')

const cachedUrl = (url) => {
    let directory = 'cached_html'
    ensurePath(directory)
    let cacheFile = directory + '/' + url.split('?')[1] + '.html'
    let exsits = fs.existsSync(cacheFile)
    if (exsits) {
        let data = fs.readFileSync(cacheFile)
        return data
    } else {
        let options = {
            'headers': {
                'user-agent': userAgent,
                'cookie': cookie,
            }
        }
        let r = request.get.sync(url, options)
        let body = r.body
        fs.writeFileSync(cacheFile, body)
        return body
    }
}

const moviesFromUrl = url => {
    let body = cachedUrl(url)
    let e = cheerio.load(body)
    let movieDivs = e('.item')
    let movies = []
    for (let i = 0; i < movieDivs.length; i++) {
        let div = movieDivs[i]
        let m = movieFromDiv(div)
        movies.push(m)
    }
    return movies
}

const saveMovie = (movies) => {
    let s = JSON.stringify(movies, null, 2)
    let path = 'douban.json'
    fs.writeFileSync(path, s)
}

const downloadCovers = (movies) => {
    let coverPath = 'covers'
    ensurePath(coverPath)
    const request = require('request')
    for (let i = 0; i < movies.length; i++) {
        let m = movies[i]
        let url = m.coverUrl
        let ranking = m.ranking
        let name = m.name.split(' / ')[0]
        let path = `${coverPath}/${ranking}_${name}.jpg`
        request(url).pipe(fs.createWriteStream(path))
    }
}


const __main = () => {
    let movies = []
    let pages = 10
    for (let i = 0; i < pages; i++) {
        let start = 25 * i
        let url = `https://movie.douban.com/top250?start=${start}&filter=`
        let moviesInPage = moviesFromUrl(url)
        movies = [...movies, ...moviesInPage]
    }
    saveMovie(movies)
    // downloadCovers(movies)
    log('抓取成功, 数据已经写入到 douban.json中')
}

__main()