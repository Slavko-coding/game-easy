input.onButtonPressed(Button.A, function () {
    sprite.turn(Direction.Left, 90)
    music.play(music.createSoundExpression(WaveShape.Square, 1400, 600, 255, 0, 100, SoundExpressionEffect.Warble, InterpolationCurve.Logarithmic), music.PlaybackMode.UntilDone)
})
input.onButtonPressed(Button.AB, function () {
    sprite.move(1)
    music.play(music.createSoundExpression(WaveShape.Square, 1, 600, 255, 0, 100, SoundExpressionEffect.Warble, InterpolationCurve.Logarithmic), music.PlaybackMode.UntilDone)
    if (sprite.isTouching(sprite_food)) {
        score += 1
        sprite_food.delete()
        music.play(music.createSoundExpression(WaveShape.Square, 5000, 803, 255, 151, 350, SoundExpressionEffect.None, InterpolationCurve.Logarithmic), music.PlaybackMode.UntilDone)
        sprite_food = game.createSprite(randint(0, 5), randint(0, 5))
    }
    if (score == 10) {
        sprite_food.delete()
        sprite.delete()
        for (let index = 0; index < 3; index++) {
            music._playDefaultBackground(music.builtInPlayableMelody(Melodies.Entertainer), music.PlaybackMode.InBackground)
            basic.showString("win")
        }
    }
})
input.onButtonPressed(Button.B, function () {
    sprite.turn(Direction.Right, 90)
    music.play(music.createSoundExpression(WaveShape.Square, 1400, 600, 255, 0, 100, SoundExpressionEffect.Warble, InterpolationCurve.Logarithmic), music.PlaybackMode.UntilDone)
})
let sprite_food: game.LedSprite = null
let sprite: game.LedSprite = null
let score = 0
score = 0
sprite = game.createSprite(2, 2)
sprite_food = game.createSprite(randint(0, 5), randint(0, 5))
let _4digit = grove.createDisplay(DigitalPin.P1, DigitalPin.P15)
_4digit.set(5)
basic.forever(function () {
    _4digit.show(score)
})
