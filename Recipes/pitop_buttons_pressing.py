# import modules or classes for controlling components and code from code libraries
# import the class for each button from the buttons library
# sleep lets us tell our components to wait (on or off) for a specified amount of time
from pitop import Pitop
from time import sleep
miniscreen = Pitop().miniscreen
# name the button(s) and assign the functions
# we have called our ∧ button “up”, our ∨ button “down”, our O button “select” and our X button “cancel”
up = miniscreen.up_button
down = miniscreen.down_button
select = miniscreen.select_button
cancel = miniscreen.cancel_button

# define (def) actions for each of the buttons
def up_action():
    print ("UP is pressed")

def down_action():
    print ("DOWN is pressed")

def select_action():
    print ("SELECT is pressed")

def cancel_action():
    print ("CANCEL is pressed")

# Now, the algorithm
up.when_pressed = up_action
down.when_pressed = down_action
select.when_pressed = select_action
cancel.when_pressed = cancel_action
sleep(5)