def on_button_pressed_a():
    sprite.turn(Direction.LEFT, 90)
    music.play(music.create_sound_expression(WaveShape.SQUARE,
            1400,
            600,
            255,
            0,
            100,
            SoundExpressionEffect.WARBLE,
            InterpolationCurve.LOGARITHMIC),
        music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global score, sprite_food
    sprite.move(1)
    music.play(music.create_sound_expression(WaveShape.SQUARE,
            1,
            600,
            255,
            0,
            100,
            SoundExpressionEffect.WARBLE,
            InterpolationCurve.LOGARITHMIC),
        music.PlaybackMode.UNTIL_DONE)
    if sprite.is_touching(sprite_food):
        score += 1
        sprite_food.delete()
        music.play(music.create_sound_expression(WaveShape.SQUARE,
                5000,
                803,
                255,
                151,
                350,
                SoundExpressionEffect.NONE,
                InterpolationCurve.LOGARITHMIC),
            music.PlaybackMode.UNTIL_DONE)
        sprite_food = game.create_sprite(randint(0, 5), randint(0, 5))
    if score == 10:
        sprite_food.delete()
        sprite.delete()
        for index in range(3):
            music._play_default_background(music.built_in_playable_melody(Melodies.ENTERTAINER),
                music.PlaybackMode.IN_BACKGROUND)
            basic.show_string("win")
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    sprite.turn(Direction.RIGHT, 90)
    music.play(music.create_sound_expression(WaveShape.SQUARE,
            1400,
            600,
            255,
            0,
            100,
            SoundExpressionEffect.WARBLE,
            InterpolationCurve.LOGARITHMIC),
        music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.B, on_button_pressed_b)

sprite_food: game.LedSprite = None
sprite: game.LedSprite = None
score = 0
score = 0
sprite = game.create_sprite(2, 2)
sprite_food = game.create_sprite(randint(0, 5), randint(0, 5))
_4digit = grove.create_display(DigitalPin.P1, DigitalPin.P15)
_4digit.set(5)

def on_forever():
    _4digit.show(score)
basic.forever(on_forever)
