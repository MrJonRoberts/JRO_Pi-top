from time import sleep
from pitop import Pitop

# get screen
mini_screen = Pitop().miniscreen

# output

mini_screen.display_multiline_text(" Welcome to ....", font_size = 20)
sleep(4)
mini_screen.clear()
