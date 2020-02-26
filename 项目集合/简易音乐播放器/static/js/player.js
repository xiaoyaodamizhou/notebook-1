class MusicPlayer {
    constructor() {
        this.curIndex = audio.dataset.cur
        this.sum = audio.dataset.sum
        this.music = e('audio')
        this.shuffle = false
    }

    update() {
        let name = playlist[this.curIndex]
        // log('name', name)
        this.music.src = './audioStore/' + name
        let img = e('.music-list-bg img')
        img.src = `./static/imgs/${this.curIndex}.jpg`
        let bg = e('.music-bg img')
        bg.src = `./static/imgs/${this.curIndex}.jpg`
        let musicLists = es('.music-list-item')
        for (let m  of musicLists) {
            m.classList.remove('my-active')
            let path = m.dataset.path
            path = path.split('./audioStore/')[1]
            if (path === name) {
                m.classList.add('my-active')
            }
        }
        log('loadhearts')
        this.loadHearts()
    }

    play() {
        // log('play')
        this.music.play()
    }

    pause() {
        // log('pause')
        this.music.pause()
    }

    volume(size) {
        if (size < 0 || size > 0) {
            return
        }
        this.music.volume = size
    }

    loadHearts() {
        let hearts = load()
        let status = false
        for (let h of hearts) {
            let index = this.curIndex
            let heart = Number(h)
            index = Number(index)
            // log('index', index, heart)
            if (heart === index) {
                status = true
            }
        }
        let heartIcon = e('.heart i')
        // log('status', status)
        if (status) {
            heartIcon.classList.remove('icon-heart1')
            heartIcon.classList.add('icon-heart')
        } else {
            heartIcon.classList.remove('icon-heart')
            heartIcon.classList.add('icon-heart1')
        }
    }

    timeUpdate() {
        let music = this.music
        // log('music', music, music.duration)
        music.addEventListener('timeupdate', () => {
            let duration = music.duration
            // log('duration', music.duration)
            duration = Number(duration)
            // log('timeupdate')
            let progress = e('.music-progress-success')
            let curTime = music.currentTime
            curTime = Number(curTime)
            // log('cure', curTime, duration)
            let baifenbi = curTime / duration
            // log('baifenbi', baifenbi)
            baifenbi = parseFloat(baifenbi).toFixed(2)
            let s = baifenbi * 100 + '%'
            // log('s', s)
            $(progress).css('width', s)
        })
    }

    ended() {
        if (this.music.ended) {
            // log('player ended')
            this.music.pause()
            if (this.shuffle) {
                this.curIndex = getRandom()
            } else {
                let index = this.curIndex
                let sum = this.sum
                // log('this', this)
                // log('index', index, sum, this.curIndex)
                index = Number(index)
                sum = Number(sum)
                index = (index + sum + 1) % sum
                // log('update index', index, this.curIndex)
                if (index === 0) {
                    index = sum
                }
                this.curIndex = index
            }
        }
    }

}