#//////////////////////// SERVO CONTROL ///////////////////////

from pitop import Pitop, DriveController, PanTiltController
from time import sleep

# Create a basic robot
robot = Pitop()
drive = DriveController(left_motor_port="M3",
                        right_motor_port="M0")
robot.add_component(PanTiltController(servo_pan_port= "S0",
                                       servo_tilt_port= "S3"))

robot.add_component(drive)
robot.pan_tilt.calibrate()

robot.pan_tilt.tilt_servo.target_angle = 25
robot.pan_tilt.pan_servo.target_angle = -10

sleep(2)