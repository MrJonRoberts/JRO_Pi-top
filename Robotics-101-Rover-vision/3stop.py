#////////////////// HOLD AND STOP ROTATION ////////////////
from pitop import Pitop, DriveController
from time import sleep

# Create a basic robot
robot = Pitop()
drive = DriveController(left_motor_port="M3",
                        right_motor_port="M0")
robot.add_component(drive)


robot.drive.forward(0.25, hold=True)
sleep(2)
robot.drive.left(0.1)
sleep(2)
robot.drive.stop_rotation()
sleep(2)
robot.drive.stop()