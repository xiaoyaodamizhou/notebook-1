class GuaCanvas extends GuaObject {
    constructor(selector) {
        super()
        let canvas = _e(selector)
        this.canvas = canvas
        this.context = canvas.getContext('2d')
        this.w = canvas.width
        this.h = canvas.height
        this.pixels = this.context.getImageData(0, 0, this.w, this.h)
        this.pixelsLength = this.pixels.data.length
        this.bytesPerPixel = 4
        this.store = []

    }

    setColor(r, g, b, a) {
        this.drawColor = GuaColor.setColor(r, g, b, a)
    }

    // 刷新页面
    render() {
        let {pixels, context} = this
        context.putImageData(pixels, 0, 0)
    }

    _setPixel(x, y, color) {
        let int = Math.floor
        x = int(x)
        y = int(y)
        let i = (y * this.w + x) * this.bytesPerPixel
        let p = this.pixels.data
        let {r, g, b, a} = color
        p[i] = r
        p[i + 1] = g
        p[i + 2] = b
        p[i + 3] = a
    }

    clear(color = GuaColor.white()) {
        let {w, h} = this
        for (let x = 0; x < w; x++) {
            for (let y = 0; y < h; y++) {
                this._setPixel(x, y, color)
            }
        }
        this.render()
    }

    fillColor(upperLeft, w, h, color = GuaColor.white()) {
        for (let x = upperLeft.x; x < w+upperLeft.x; x++) {
            for (let y = upperLeft.y; y < h+upperLeft.y; y++) {
                this._setPixel(x, y, color)
            }
        }
        let pixels = this.pixels
        this.render()
    }


    drawPoint(point, color = GuaColor.black()) {
        let {w, h} = this
        let p = point
        if (p.x >= 0 && p.x <= w) {
            if (p.y >= 0 && p.y <= h) {
                this._setPixel(p.x, p.y, color)
            }
        }
        this.render()
    }

    drawLine(p1, p2, color = GuaColor.black(), width = 1) {
        let {w, h} = this
        let k = (p2.y - p1.y) / (p2.x - p1.x)
        let n = Math.max(p1.x, p2.x)
        let m = Math.min(p1.x, p2.x)
        for (let x = m; x <= n; x++) {
            let y = k * (x - p2.x) + p2.y
            let point = GuaPoint.new(x, y)
            this.drawPoint(point, color)
        }
        if (p1.x === p2.x) {
            for (let y = p1.y; y <= p2.y; y++) {
                let x = p1.x
                let point = GuaPoint.new(x, y)
                this.drawPoint(point, color)
            }
        }
    }

    drawRect(upperLeft, size, fillColor = null, borderColor = GuaColor.black()) {
        let [x1, y1] = [upperLeft.x, upperLeft.y]
        let [x2, y2] = [upperLeft.x + size.w, upperLeft.y]
        let [x3, y3] = [upperLeft.x, upperLeft.y + size.h]
        let [x4, y4] = [upperLeft.x + size.w, upperLeft.y + size.h]
        let [p1, p2, p3, p4] = [GuaPoint.new(x1, y1), GuaPoint.new(x2, y2),
            GuaPoint.new(x3, y3), GuaPoint.new(x4, y4)]
        this.drawLine(p1, p2, borderColor)
        this.drawLine(p1, p3, borderColor)
        this.drawLine(p2, p4, borderColor)
        this.drawLine(p3, p4, borderColor)
    }


    __debug_draw_demo() {
        let {context, pixels} = this
        let data = pixels.data
        for (let i = 0; i < data.length; i += 4) {
            let [r, g, b, a] = data.slice(i, i + 4)
            r = 255
            a = 255
            data[i] = r
            data[i + 3] = a
        }
        context.putImageData(pixels, 0, 0)
    }
}
