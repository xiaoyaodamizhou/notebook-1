var randomBetween = function(start, end){
    var n = (start + Math.random() * (end - start))
    return n
}

class Scene extends GuaScene {
    constructor(game) {
        super(game)
        this.game = game
        this.setup()
        this.setupInputs()
    }

    // 添加元素pipe, bird, background, ground
    setup(){
        var game = this.game
        // 背景
        var bg = GuaImage.new(game,'bg')
        this.addElement(bg)

        // 人物动画
        var w = GuaAnimation.new(game)
        w.x = 100
        w.y = game.canvas.height / 2
        this.addElement(w)
        this.w = w
        this.setupInputs()

        // 接入水管
        var pipes = Pipes.new(game)
        this.pipes = pipes
        this.addElement(pipes)

        // 滚动背景-地面
        this.grounds = []
        for(var i = 0; i <= 30; i++){
            var g = GuaImage.new(game, 'ground')
            g.x = i * g.w
            g.y = game.canvas.height - g.h
            window.groundHeight = g.y
            this.addElement(g)
            this.grounds.push(g)
        }
        this.skipCount = 5

        // 显示小鸟的生命数， 游戏分数
        this.lifes = 3
        this.score = 0

    }

    draw(){
        super.draw()
        var context = this.game.context
        context.fillStyle = 'black'
        context.fillText('score: '+ this.score, 10, 40)
    }

    update(){
        // super.update(),调用父类的update函数
         if (window.paused) {
            return
        }

        super.update()
        enableFps()

        this.skipCount--
        var offset = -2
        if(this.skipCount == 0){
            this.skipCount = 5
            offset = (this.skipCount - 1) * (-offset)
        }
         // 地面移动
        for(var i = 0; i <= 30; i++){
            var g = this.grounds[i]
            g.x += offset
        }

        if(this.w.y + this.w.h > window.groundHeight){
            //log('坠地')
            playNow('die')
            window.count = 0
            var end = SceneEnd.new(this.game)
            this.game.replaceScene(end)
        }

        if(this.pipes.collide(this.w) == 'collide'){
            //log('相撞')
            playNow('collide')
            window.count = 0
            var end = SceneEnd.new(this.game)
            this.game.replaceScene(end)
        }

        this.pipes.passCount(this.w)
        this.score = 100 * window.count
    }

    setupInputs(){
        // 添加指令
        var self = this
        var enableDrag = false
        this.game.registerAction('a', function(){
            // event-'down','up'
            var x = config.bird_speed.value
            self.w.move(-x)
        })
        this.game.registerAction('d', function(){
            var x = config.bird_speed.value
            self.w.move(x)
        })

        this.game.registerAction('j', function(){
            self.w.jump()
        })

        this.game.canvas.addEventListener('mousedown', function(event) {
            var x = event.offsetX
            var y = event.offsetY
            //log(x, y, event)
            // 检查是否点中了 bird
            // log('this.w', this.w)
            if (self.w.hasPoint(x, y)) {
                // 设置拖拽状态
                enableDrag = true
            }
        })
        this.game.canvas.addEventListener('mousemove', function(event) {
            var x = event.offsetX
            var y = event.offsetY
            // log(x, y, 'move')
            if (enableDrag) {
                self.w.x = x
                self.w.y = y
            }
        })
        this.game.canvas.addEventListener('mouseup', function(event) {
            var x = event.offsetX
            var y = event.offsetY
            enableDrag = false
        })

    }


}


