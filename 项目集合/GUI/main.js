let GuaSelectColor = _e('.gua-selecttColor')

let defaultColor = GuaColor.red()

let drawBtns = es('.draw-Btn')
let select = _e('.select-wrapper')

let toolback = _e('.gua-tool-back')
let toolclear = _e('.gua-tool-clear')

let canvas = _e('#id-canvas')
let context = canvas.getContext('2d')
let guaCanvas = GuaCanvas.new('#id-canvas')

let status = false
let pre = {}
let btns = []

let rectPoints = [{
    "upperleft": GuaPoint.new(0, 0),
    "size": GuaSize.new(400, 300)
}]

function origin(){
    guaCanvas.clear()
    const ori = context.getImageData(0, 0, 400, 300)
    return ori
}

const ORIGINAL = origin()

// 存储每次的画布状态
let store = [ORIGINAL]

const save = function(){
    let current = context.getImageData(0, 0, 400, 300)
    store.push(current)
    log('save', store)
}

const reback = function(w, h) {
    if (store.length !== 1) {
        store.pop()
        let prevent = store[store.length-1]
        guaCanvas.pixels = prevent
        guaCanvas.render()
    } else {
        guaCanvas.clear()
        log('store is 1', store)
        guaCanvas.pixels = store[0]
        guaCanvas.render()
    }
}

const clear = function () {
    guaCanvas.clear()
}

// p鼠标当前的坐标
const hasPoint = function (p, reference) {
    let {upperleft, size} = reference
    if (upperleft.x <= p.x && p.x <= upperleft.x + size.w) {
        if (upperleft.y <= p.y && p.y <= upperleft.y + size.h) {
            return true
        }
    }
    return false
}

const minBlock = function (p) {
    let points = []
    for (var point of rectPoints) {
        if (hasPoint(p, point)) {
            points.push(point)
        }
    }
    let min = points[0]
    for (var point of points) {
        if (min.size.w * min.size.h > point.size.w * point.size.h) {
            min = point
        }
    }
    return min
}

const selectColor = function () {
    for (var c of GuaSelectColor.children) {
        bindEvent(c, 'click', function (event) {
            let target = event.target
            let color = target.dataset.color
            let {r, g, b, a} = changeColor(color)
            defaultColor = GuaColor.setColor(r, g, b, a)
        })
    }
}


let [penline, drawline, drawrect, patternfill, drawBtn] = drawBtns



const selectTool = function () {
    toolclear.addEventListener('click', function () {
        log('clear')
        clear()
    })
    toolback.addEventListener('click', function () {
        log('back')
        reback()
    }, true)
}

//////////////
var eventPatternFillColor = function (event) {
    let [x, y] = [event.offsetX, event.offsetY]
    let p = GuaPoint.new(x, y)
    let minblock = minBlock(p)
    guaCanvas.fillColor(minblock.upperleft, minblock.size.w, minblock.size.h, defaultColor)
    save()
}

////////////////////////////////
var eventPenLineDown = function (event) {
    status = true
    startX = event.offsetX
    startY = event.offsetY
    point1 = GuaPoint.new(startX, startY)
    guaCanvas.drawPoint(point1, defaultColor)
}

var eventPenLineMove = function (event) {
    if (status) {
        let [moveX, moveY] = [event.offsetX, event.offsetY]
        let point = GuaPoint.new(moveX, moveY)
        guaCanvas.drawPoint(point, defaultColor)
    }
}

var eventPenLineUp = function (event) {
    status = false
    endX = event.offsetX
    endY = event.offsetY
    point2 = GuaPoint.new(endX, endY)
    guaCanvas.drawPoint(point2, defaultColor)
    save()
}

///////
var eventDrawLineDown = function (event) {
    [startX, startY] = [event.offsetX, event.offsetY]
    point1 = GuaPoint.new(startX, startY)
}

var eventDrawLineUp = function (event) {
    [endX, endY] = [event.offsetX, event.offsetY]
    point2 = GuaPoint.new(endX, endY)
    guaCanvas.drawLine(point1, point2, defaultColor)
    save()
}

/////////
var eventDrawRectDown = function (event) {
    [startX, startY] = [event.offsetX, event.offsetY]
    upperLeft = GuaPoint.new(startX, startY)
}

var eventDrawRectUp = function (event) {
    [endX, endY] = [event.offsetX, event.offsetY]
    w = endX - startX
    h = endY - startY
    size = GuaSize.new(w, h)
    guaCanvas.drawRect(upperLeft, size, defaultColor, defaultColor)
    rectPoints.push({'upperleft': upperLeft, 'size': size})
    save()
}
/////////////

var eventDrawBtnDown = function (event) {
    [startX, startY] = [event.offsetX, event.offsetY]
    upperLeft = GuaPoint.new(startX, startY)
}

var eventDrawBtnUp = function (event) {
    [endX, endY] = [event.offsetX, event.offsetY]
    w = endX - startX
    h = endY - startY
    size = GuaSize.new(w, h)
    guaCanvas.drawRect(upperLeft, size, defaultColor, defaultColor)
    btn = GuaButton.new(startX, startY, w, h)
    btns.push(btn)
    save()
}



const removeCanvasEvents = function() {
    canvas.removeEventListener('mousedown', eventPatternFillColor)
    canvas.removeEventListener('mouseup', eventDrawRectUp)
    canvas.removeEventListener('mousedown', eventDrawRectDown)
    canvas.removeEventListener('mouseup', eventPenLineUp)
    canvas.removeEventListener('mousemove', eventPenLineMove)
    canvas.removeEventListener('mousedown', eventPenLineDown)
    canvas.removeEventListener('mouseup', eventDrawLineUp)
    canvas.removeEventListener('mousedown', eventDrawLineDown)
    canvas.removeEventListener('mouseup', eventDrawBtnUp)
    canvas.removeEventListener('mousedown', eventDrawBtnDown)
}

// 油漆桶实现
var patternFillColor = function () {
    console.log('fillcolor')
    removeCanvasEvents()
    canvas.addEventListener('mousedown', eventPatternFillColor)
}

//画笔实现
var penLine = function () {
    console.log('penline')
    let [startX, startY] = [0, 0]
    let [endX, endY] = [0, 0]
    let [moveX, moveY] = [0, 0]

    removeCanvasEvents()
    canvas.addEventListener('mousedown', eventPenLineDown)
    canvas.addEventListener('mousemove', eventPenLineMove)
    canvas.addEventListener('mouseup', eventPenLineUp)
}

// 直线
var drawLine = function () {
    console.log('drawline')
    let [startX, startY] = [0, 0]
    let [endX, endY] = [0, 0]

    removeCanvasEvents()
    canvas.addEventListener('mousedown', eventDrawLineDown)
    canvas.addEventListener('mouseup', eventDrawLineUp)
}

// removeEventListener()
var drawRect = function () {
    console.log('drawrect')
    let [startX, startY] = [0, 0]
    let [endX, endY] = [0, 0]
    let upperLeft = {}
    let [w, h] = [0, 0]
    let size = {}

    removeCanvasEvents()
    canvas.addEventListener('mousedown', eventDrawRectDown)
    canvas.addEventListener('mouseup', eventDrawRectUp)
}

var drawButton = function() {
    console.log('drawButton')
    let [startX, startY] = [0, 0]
    let [endX, endY] = [0, 0]
    let upperLeft = {}
    let [w, h] = [0, 0]
    let size = {}

    removeCanvasEvents()
    canvas.addEventListener('mousedown', eventDrawBtnDown)
    canvas.addEventListener('mouseup', eventDrawBtnUp)
}

const removeEvents = function() {
    penline.removeEventListener('click', penLine)
    drawline.removeEventListener('click', drawLine)
    drawrect.removeEventListener('click', drawRect)
    patternfill.removeEventListener('click', patternFillColor)
    drawBtn.removeEventListener('click', drawButton)
}

const selectPattern = function () {
    select.addEventListener('click', function(event) {
        console.log('select pattern')
        let target = event.target
        if (target === penline) {
            removeEvents()
            penline.addEventListener('click', penLine)
        } else if (target === drawline) {
            removeEvents()
            drawline.addEventListener('click', drawLine)
        } else if (target === drawrect) {
            removeEvents()
            drawrect.addEventListener('click', drawRect)
        } else if (target === patternfill){
            removeEvents()
            patternfill.addEventListener('click', patternFillColor)
        } else {
            removeEvents()
            drawBtn.addEventListener('click', drawButton)
        }
    }, true)
}

const toggleBtns = function() {
    for (var btn of btns) {
        btn.addClickAction(canvas, function(){
            log('toggle')
            let [x, y, w, h] = btn
            let p = GuaPoint.new(x, y)
            guaCanvas.fillColor(p, w, h, defaultColor)
        })
    }
}

const __main = function () {
    selectColor()
    selectPattern()
    selectTool()
    toggleBtns()
}

__main()