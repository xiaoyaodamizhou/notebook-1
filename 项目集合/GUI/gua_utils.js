const log = console.log.bind(console)

const _e = (sel) => document.querySelector(sel)

const es = (sel) => document.querySelectorAll(sel)

const bindEvent = (element, eventName, callback) => {
    element.addEventListener(eventName, callback, true)
}

const appendHtml = (element, html) => {
    element.insertAdjacentHTML('beforeend', html)
}

const bindEventDelegate = (element, eventName, responseClassDict, self) => {
    element.addEventListener(eventName, function(event){
        let target = event.target
        let responseClass = target.classList[0]
        let callback = responseClassDict[responseClass]
        if(callback !== undefined){
            callback(event, self)
        }
    })
}

const changeColor = (color) => {
    color = color.substring(1)
    let r = parseInt(color.substring(0, 2), 16)
    let g = parseInt(color.substring(2, 4), 16)
    let b = parseInt(color.substring(4, 6), 16)
    let a = parseInt(color.substring(6, 8), 16)
    return {r: r, g: g, b:b, a:a}
}

const zeroArray = (length) => {
    var r = []
    for(let k = 0; k < length; k++) {
        r[k] = 0
    }
    return r
}