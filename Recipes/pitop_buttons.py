# import modules or classes for controlling components and code from code libraries
# import the PMA Led and the PMA Button classes from the pma library (PMA = pi-top Maker Architecture)
# import the functions for each button from the miniscreen library
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


# define (def) actions for each of the PMA components
def red_on():
    red.on()
    print("RED ON")


def red_off():
    red.off()
    print("RED OFF")


def yellow_on():
    yellow.on()
    print("YELLOW ON")


def yellow_off():
    yellow.off()
    print("YELLOW OFF")


def green_on():
    green.on()
    print("GREEN ON")


def green_off():
    green.off()
    print("GREEN OFF")


def buzzer_on():
    buzzer.on()
    print("BUZZ")


def buzzer_off():
    buzzer.off()
    print("NO BUZZ")


# Now, the algorithm
up.when_pressed = red_on
up.when_released = red_off
down.when_pressed = yellow_on
down.when_released = yellow_off
select.when_pressed = green_on
select.when_released = green_off
cancel.when_pressed = buzzer_on
cancel.when_released = buzzer_off
sleep(10)