class GuaButton extends GuaObject{
    constructor(x, y, w, h) {
        super()
        this.x = x
        this.y = y
        this.w = w
        this.h = h
    }

    addClickAction(canvas, clickCallback) {
        // 判断click了没有
        // 调用clickCallback
        canvas.addEventListener('click', function (event) {
            let [startX, startY] = [event.offsetX, event.offsetY]
            if (this.x <= startX && startX <= this.x + this.w) {
                if (this.y <= startY && startY <= this.y + h) {
                    clickCallback()
                }
            }
        })
    }
}