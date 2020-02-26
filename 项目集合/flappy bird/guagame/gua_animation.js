class GuaAnimation{
    constructor(game){
        this.game = game
        this.frames = []
        for(var i = 1; i <= 4; i++){
            var name = `b${i}`
            var t = game.textureByName(name)
            this.frames.push(t)
        }
        this.texture = this.frames[0]
        this.w = this.texture.width
        this.h = this.texture.height
        this.frameIndex = 0
        this.frameCount = 3

        this.flipx = false
        this.rotation = 0
        // 图片透明度
        //this.alpha = 1
        // 重力和加速度
        this.gy = 10
        this.vy = 0
    }

    static new(game){
        return new this(game)
    }
    jump(){
        playNow('jump')
        this.vy = -config.bird_jump.value
        this.rotation = -45
    }

    update(){
        // 更新alpha
        //if(this.alpha > 0){
        //    this.alpha -= 0.05
        //}
        // 更新受力
        this.y += this.vy
        this.vy += this.gy * 0.2
        if(this.y > window.groundHeight){
            this.y = window.groundHeight - this.h
        }
        //更新角度
        if(this.rotation <= 45){
            this.rotation += 5
        }
        // 帧数停留结束切换图片
        this.frameCount--
        if(this.frameCount == 0){
            this.frameCount = 3
            this.frameIndex = (this.frameIndex + 1) % this.frames.length
            this.texture = this.frames[this.frameIndex]
        }
    }

    draw(){
        var context = this.game.context
        context.save()

        var w2 = this.w / 2
        var h2 = this.h / 2
        context.translate(this.x + w2, this.y + h2)
        if(this.flipx){
            context.scale(-1, 1)
        }
        context.rotate(this.rotation * Math.PI / 180)
        context.translate(-w2, -h2)
        context.drawImage(this.texture, 0, 0)
        context.restore() 
    }

    move(x){
        var self = this
        this.flipx = x < 0
        self.x += x
    }

    hasPoint(x, y) {
        var self = this
        var xIn = x >= self.x && x <= self.x + self.w
        var yIn = y >= self.y && y <= self.y + self.h
        // log('haspoint', xIn && yIn)
        return xIn && yIn
    }

}