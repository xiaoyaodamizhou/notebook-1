const log = console.log.bind(console)

const e = selector => document.querySelector(selector)

const es = selector => document.querySelectorAll(selector)

// key对应图片，value对应歌名
const playlist = {
    '1': 'Red.mp3',
    '2': '七里香.mp3',
    '3': '星晴.mp3',
    '4': '月光.mp3',
    '5': '海阔天空.mp3',
    '6': '稻香.mp3',
    '7': '菊花台.mp3',
    '8': 'k歌之王.mp3',
}

let audio = e('.audio-cur')
localStorage.hearts = []

const getRandom = () => {
    let range = Math.random() * 8 + 1
    let index = Math.floor(range)
    return index
}

// let allHearts = []
// allHearts = JSON.stringify(allHearts)
// localStorage.hearts = allHearts

const save = function(array) {
    log('save')
    let s = JSON.stringify(array)
    localStorage.hearts = s
}

const load = function(){
    var s = localStorage.hearts
    if (!localStorage.hearts) {
        return []
    }
    return JSON.parse(s)
}