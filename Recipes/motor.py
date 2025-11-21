from time import sleep

from pitop import BrakingType, EncoderMotor, ForwardDirection

# Setup the motor

motor = EncoderMotor("M0", ForwardDirection.COUNTER_CLOCKWISE)
motor.braking_type = BrakingType.COAST


# Move in both directions

rpm_speed = 100
for _ in range(4):
    motor.set_target_rpm(rpm_speed)
    sleep(2)
    motor.set_target_rpm(-rpm_speed)
    sleep(2)

motor.stop()



from time import sleep

# Setup the motor
motor = EncoderMotor("M0", ForwardDirection.CLOCKWISE)

#Setting braking_type will change the way the motor stops.
#BrakingType.COAST will make the motor coast to a halt when stopped.
#BrakingType.BRAKE will cause the motor to actively brake when stopped.
#In practice you may not notice much. It's subtle to say the least.
motor.braking_type = BrakingType.COAST


# Move in both directions
rpm_speed = 100 #the max value is 140
for _ in range(4):
    motor.set_target_rpm(rpm_speed)
    sleep(2)
    motor.set_target_rpm(-rpm_speed) #set rpm negative to reverse the motor
    sleep(2)

motor.stop()

# forward
# from pitop.pma import EncoderMotor, ForwardDirection, BrakingType
from time import sleep

# first we set up the motors, this gives us functions to control the robot
# note that the motor objects have ForwardDirection set oposite to eachother.
motor_left = EncoderMotor("M0", ForwardDirection.COUNTER_CLOCKWISE)
motor_left.braking_type = BrakingType.COAST
motor_right = EncoderMotor("M3", ForwardDirection.CLOCKWISE)
motor_right.braking_type = BrakingType.COAST


def drive(target_rpm: float):
    print("Start driving at target", target_rpm, "rpm...")
    motor_left.set_target_rpm(target_rpm)
    motor_right.set_target_rpm(target_rpm)


def stop():
    motor_right.stop()
    motor_left.stop()


rpm_speed = 100
drive(rpm_speed)
sleep(5)
stop()
