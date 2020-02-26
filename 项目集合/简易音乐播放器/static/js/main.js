class Events {
    constructor(player) {
        this.player = player
    }

    playEvent(target) {
        if (target.classList.contains('icon-play2')) {
            this.player.play()
            target.classList.remove('icon-play2')
            target.classList.add('icon-pause')
        } else if (target.classList.contains('icon-pause')) {
            this.player.pause()
            target.classList.remove('icon-pause')
            target.classList.add('icon-play2')
        }
    }

    playEvent2(target) {
        if (target.classList.contains('icon-play2')) {
            target.classList.remove('icon-play2')
            target.classList.add('icon-pause')
        }
        this.player.play()
    }

    bindEventChooseMusic() {
        let musicList = e('.music-list')
        musicList.addEventListener('click', (event) => {
            // log('click choose')
            let target = event.target
            if (target.classList.contains('music-list-item')) {
                let path = target.dataset.path
                path = path.split('./audioStore/')[1]
                // log('path', path)
                let index = Object.entries(playlist).find((val) => {
                    let [k, v] = val
                    return v === path
                })
                index = index[0]
                this.player.curIndex = index
                this.player.update()
                let icon = e('.play i')
                this.playEvent2(icon)
            }
        })
    }

    bindEventPlay() {
        let playBtn = e('.play')
        playBtn.addEventListener('click', (event) => {
            let target = event.target
            this.playEvent(target)
        })
    }

    bindEventBackward() {
        let backward = e('.backward')
        backward.addEventListener('click', (event) => {
            let index = 0
            if (this.player.shuffle) {
                index = getRandom()
            } else {
                index = this.player.curIndex
                let sum = this.player.sum
                sum = Number(sum)
                index = Number(index)
                index = (index + sum - 1) % sum
                if (index === 0) {
                    index = sum
                }
            }
            this.player.curIndex = index
            this.player.update()
            let icon = e('.play i')
            this.playEvent2(icon)
        })
    }

    bindEventforward() {
        let backward = e('.forward')
        backward.addEventListener('click', (event) => {
            let index = 0
            if (this.player.shuffle) {
                index = getRandom()
            } else {
                index = this.player.curIndex
                let sum = this.player.sum
                sum = Number(sum)
                index = Number(index)
                index = (index + sum + 1) % sum
                if (index === 0) {
                    index = sum
                }
            }
            this.player.curIndex = index
            this.player.update()
            let icon = e('.play i')
            this.playEvent2(icon)
        })
    }

    bindEventVolume() {
        let volume = e('.volume i')
        let status = false
        volume.addEventListener('click', (event) => {
            status = !status
            let range = e('.range')
            if (status) {
                range.classList.remove('hide')
                range.classList.add('show')
                let input = e('.input-range')
                input.addEventListener('change', (event) => {
                    let value = Number(input.value)
                    this.player.music.volume = value
                })
            } else {
                range.classList.remove('show')
                range.classList.add('hide')
            }
        })
    }

    bindEventloop() {
        let loop = e('.loop')
        loop.addEventListener('click', (event) => {
            let target = event.target
            if (target.classList.contains('icon-loop')) {
                this.player.shuffle = true
                // log('shuffle', this.player.shuffle)
                target.classList.remove('icon-loop')
                target.classList.add('icon-shuffle')
            }
            else if (target.classList.contains('icon-shuffle')) {
                this.player.shuffle = false
                // log('shuffle', this.player.shuffle)
                target.classList.remove('icon-shuffle')
                target.classList.add('icon-loop')
            }
        })
    }

    bindEventCollect() {
        let heart = e('.heart')
        heart.addEventListener('click', (event) => {
            let target = event.target
            let index = this.player.curIndex
            let hearts = load()
            // log('hearts', hearts)
            let status = hearts.find(val => {
                return val === index
            })
            if (status === undefined) {
                hearts.push(index)
                target.classList.remove('icon-heart1')
                target.classList.add('icon-heart')
                save(hearts)
            } else {
                let i = 0
                for (i; i < hearts.length; i++) {
                    let heart = hearts[i]
                    if (heart === index) {
                        break
                    }
                }
                hearts.splice(i, 1)
                target.classList.remove('icon-heart')
                target.classList.add('icon-heart1')
                save(hearts)
            }
        })
    }

    bindEventEnd() {
        let music = this.player.music
        let player = this.player
        music.addEventListener('ended', () => {
            // log('evnet ended start')
            player.ended.bind(player)()
            // log('evnet ended end')
            player.update()
            player.play()
        })
    }
    bindEvents() {
        this.bindEventChooseMusic()
        this.bindEventPlay()
        this.bindEventBackward()
        this.bindEventforward()
        this.bindEventVolume()
        this.bindEventloop()
        this.bindEventCollect()
        this.bindEventEnd()
    }
}

// let player = new MusicPlayer()
// player.music.playbackRate = 15
// player.loadHearts()
// player.timeUpdate()
// let events = new Events(player)
// events.bindEvents()

const __main = () => {
    let player = new MusicPlayer()
    // player.music.playbackRate = 15
    player.loadHearts()
    player.timeUpdate()
    let events = new Events(player)
    events.bindEvents()
}

__main()
