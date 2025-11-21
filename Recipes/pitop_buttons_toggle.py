from pitop.pma import LED, Buzzer
from pitop import Pitop
from time import sleep
miniscreen = Pitop().miniscreen

# name the LEDs and the buttons and state which ports the LEDs are connected to
red = LED("D0")
yellow = LED("D1")
green = LED("D2")
buzzer = Buzzer("D3")
up = miniscreen.up_button
down = miniscreen.down_button
select = miniscreen.select_button
cancel = miniscreen.cancel_button

# Now, the algorithm
# create a loop. Everything 'inside' (indented underneath) will continually repeat until the program is stopped
while True:
    up.when_pressed = red.toggle
    down.when_pressed = yellow.toggle
    select.when_pressed = green.toggle
    cancel.when_pressed = buzzer.toggle