class GuaScene {
    constructor(game) {
        this.game = game
        this.elements = []
        this.debugModeEnabled = true
    }
    static new(game) {
        var i = new this(game)
        return i
    }
    addElement(guaImage){
        guaImage.scene = this
        this.elements.push(guaImage)
    }
    draw() {
        for(var i = 0; i < this.elements.length; i++){
            var e = this.elements[i]
            //this.game.drawImage(e)
            // 图片自己画自己
            e.draw()
        }
    }
    update() {
        if(this.debugModeEnabled){
            for(var i = 0; i < this.elements.length; i++){
                var e = this.elements[i]
                e.debug && e.debug()
            }
        }

        for(var i = 0; i < this.elements.length; i++){
            this.elements[i].update()
        }
    }
}
