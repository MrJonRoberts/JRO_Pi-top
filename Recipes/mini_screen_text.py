from time import sleep
from pitop import Pitop

# get screen
mini_screen = Pitop().miniscreen

# output

mini_screen.display_multiline_text(" Welcome to ....", font_size = 20)
sleep(4)
mini_screen.clear()

from pitop import Pitop
from time import sleep

mini_screen = Pitop().miniscreen
select = mini_screen.select_button

# while True: creates a loop. Each time the select button is pressed, the 3 messages will appear on the OLED screen
while True:
    if select.is_pressed:
        mini_screen.display_multiline_text("Hello", font_size=10)
        sleep(3)

        mini_screen.clear()
        mini_screen.display_multiline_text("Welcome to your pi-top [4]", font_size=15)
        sleep(3)

        mini_screen.clear()
        mini_screen.display_multiline_text("What will you make today?", font_size=20)
        sleep(3)

        mini_screen.clear()