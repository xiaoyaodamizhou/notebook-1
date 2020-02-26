// 记录小鸟的通过次数
window.count = 0

class Pipes{
    constructor(game){
        this.game = game
        this.pipes = []
        this.pipeSpace = 150
        this.pipeDistance = 200
        this.columsOfPipe = 3
        for(var i = 0; i < this.columsOfPipe; i++){
            var p1 = GuaImage.new(game, 'pipe1')
            p1.x = game.canvas.width + i * this.pipeDistance
            var p2 = GuaImage.new(game, 'pipe2')
            p2.x = p1.x
            this.resetPipesPosition(p1, p2)
            this.pipes.push(p1)
            this.pipes.push(p2)
        }
    }

    static new(game){
        return new this(game)
    }

    resetPipesPosition(p1, p2){
        p1.y = randomBetween(-250, 0)
        p2.y = (p1.y + p1.h + this.pipeSpace)
    }

    debug(){
        this.pipeSpace = config.pipe_space.value
        this.pipeDistance = config.pipe_distance.value
    }

    update(){
        for(var i = 0; i < this.pipes.length; i+=2){
            var p1 = this.pipes[i]
            var p2 = this.pipes[i+1]
            p1.x -= 5
            p2.x -= 5
            if(p1.x < - 100){
                p1.x += this.pipeDistance * this.columsOfPipe
            }
            if(p2.x < - 100){
                p2.x += this.pipeDistance * this.columsOfPipe
                this.resetPipesPosition(p1, p2)
            }
        }
    }

    draw(){
        var context = this.game.context
        for(var p of this.pipes){
            context.save()

            var w2 = p.w / 2
            var h2 = p.h / 2
            context.translate(p.x + w2, p.y + h2)
            if(this.flipx){
                context.scale(-1, 1)
            }
            //context.globalAlpha = this.alpha
            context.rotate(p.rotation * Math.PI / 180)
            context.translate(-w2, -h2)
            context.drawImage(p.texture, 0, 0)
            context.restore()
        }
    }

    col(bird, p){
        if(aInb(p.x, bird.x, bird.x + bird.w) || aInb(bird.x, p.x, p.x+ p.w)){
            if(aInb(p.y, bird.y, bird.y+bird.h)|| aInb(bird.y, p.y, p.y+ p.h)){
                    return true
            }
        }
    }

    collide(bird){
        for(var p of this.pipes){
            if(this.col(bird, p)){
                return 'collide'
            }
        }
    }

    pass(bird, p){
        if(bird.x == p.x){
            // log('pass test', bird.x, p.x)
        }
        return bird.x == p.x && (! this.col(bird, p))
    }

    passCount(bird){
        for(var i = 0; i < this.pipes.length; i+=2){
            if(this.pass(bird, this.pipes[i]) && this.pass(bird, this.pipes[i+1])){
                window.count += 1
                log('pass')
                playNow('pass')
            }
        }
    }

}

