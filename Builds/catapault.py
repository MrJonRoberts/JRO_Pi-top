# https://further.pi-top.com/lessons/14c59529-e0db-4d91-840f-ebb6e907d0b2

#import from libraries
from pitop.pma import EncoderMotor, ForwardDirection, BrakingType
from time import sleep

#Variables
motor = EncoderMotor("M2", ForwardDirection.CLOCKWISE)
rpm_speed = 80 #rotations per minute, the max value is 114

#Code Body
motor.set_target_rpm(rpm_speed)
sleep(0.2)

