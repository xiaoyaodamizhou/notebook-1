class SceneTitle extends GuaScene {
    constructor(game) {
        super(game)
        this.game = game
        this.setup()
        this.setupInputs()
    }

    setup() {
        var label = GuaLabel.new(this.game, '按1开始游戏')
        this.addElement(label)
    }

    draw() {
        super.draw()
    }

    setupInputs() {
        var self = this
        this.game.registerAction('1', function (event) {
            var scene = Scene.new(self.game)
            self.game.replaceScene(scene)
        })
    }

    update() {
        super.update()
    }
}
