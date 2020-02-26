class SceneEnd extends GuaScene {
    constructor(game) {
        super(game)
        game.registerAction('2', function(){
            var s = SceneTitle.new(game)
            game.replaceScene(s)
        })
    }
    draw() {
        // draw labels
        var context = this.game.context
        var canvas = this.game.canvas
        context.fillStyle = 'lightblue'
        context.fillRect(0, 0, canvas.width, canvas.height)
        context.font = '30px solid'
        context.strokeStyle = 'black'
        this.game.context.strokeText('游戏结束', 100, 200)
        this.game.context.strokeText('按2返回游戏', 100, 250)
    }
}
