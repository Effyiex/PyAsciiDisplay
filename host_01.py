
import display

display.init("Host_01.py", 48, 24, 'c', '0')
display.set_frame('#', '#')

rage_x = 5

while True:

    display.background(' ')
    display.text_align("CENTER")
    display.text("*RAGE*", display.width / 2 + rage_x, display.height / 2 - 1)
    display.render(0.25)

    rage_x *= -1
