class GuaLabel{
    constructor(game, text){
        this.game = game
        this.text = text
    }
    static new(game, text){
        return new this(game, text)
    }

    draw(){
        var context = this.game.context
        context.font = 'italic small-caps bold 30px aria'
        context.strokeStyle="black";
        this.game.context.strokeText(this.text, 100, 200)
    }

    update(){

    }
}