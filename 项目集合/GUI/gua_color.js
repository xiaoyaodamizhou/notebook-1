class GuaColor extends GuaObject {
    constructor(r, g, b, a) {
        super()
        this.r = r
        this.g = g
        this.b = b
        this.a = a
    }

    static black() {
        return this.new(0, 0, 0, 255)
    }

    static white() {
        return this.new(255, 255, 255, 255)
    }

    static transparent() {
        return this.new(255, 255, 255, 0)
    }

    static red() {
        return this.new(255, 0, 0, 255)
    }

    static green() {
        return this.new(0, 255, 0, 255)
    }

    static setColor(r, g, b, a) {
        return this.new(r, g, b, a)
    }
}