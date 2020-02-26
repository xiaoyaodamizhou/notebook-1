var enableFps = function () {
    window.fps = config.timer.value
}

var __main = function () {
    var images = {
        bg: 'img/bg.png',
        ground: 'img/ground.png',
        b1: 'img/bird-01.png',
        b2: 'img/bird-02.png',
        b3: 'img/bird-03.png',
        b4: 'img/bird-04.png',
        pipe1: 'img/tube1.png',
        pipe2: 'img/tube2.png',
    }

    console.log('run')

    var game = GuaGame.instance(20, images, function (g) {
        var s = SceneTitle.new(g)
        g.runWithScene(s)
    })

    console.log('game')

}

__main()


