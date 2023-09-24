def on_gesture_shake():
    global timer
    timer = 0
    basic.show_icon(IconNames.SURPRISED)
    music.play(music.builtin_playable_sound_effect(soundExpression.giggle),
        music.PlaybackMode.UNTIL_DONE)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_logo_pressed():
    global timer
    timer = 0
    basic.show_icon(IconNames.HAPPY)
    music.play(music.builtin_playable_sound_effect(soundExpression.happy),
        music.PlaybackMode.UNTIL_DONE)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

timer = 0
timer = 0
basic.show_leds("""
    . # . # .
    . . . . .
    . . # . .
    # . . . #
    . # # # .
    """)
music.play(music.builtin_playable_sound_effect(soundExpression.hello),
    music.PlaybackMode.UNTIL_DONE)

def on_forever():
    global timer
    basic.pause(100)
    timer += 1
    if timer == 10:
        basic.show_icon(IconNames.SAD)
        music.play(music.builtin_playable_sound_effect(soundExpression.sad),
            music.PlaybackMode.UNTIL_DONE)
    if timer == 20:
        basic.show_icon(IconNames.ASLEEP)
        music.play(music.builtin_playable_sound_effect(soundExpression.yawn),
            music.PlaybackMode.UNTIL_DONE)
    if timer == 30:
        basic.show_icon(IconNames.SKULL)
        music.play(music.builtin_playable_sound_effect(soundExpression.mysterious),
            music.PlaybackMode.UNTIL_DONE)
        while True:
            basic.show_icon(IconNames.SKULL)
            music.play(music.builtin_playable_sound_effect(soundExpression.mysterious),
                music.PlaybackMode.UNTIL_DONE)
basic.forever(on_forever)
