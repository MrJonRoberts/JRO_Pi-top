# //////////////////////// CAMERA DIRECTION ///////////////////////
from pitop import Pitop, DriveController, Camera, PanTiltController
from time import sleep
from further_link import send_image
from signal import pause
from pitop.processing.algorithms.line_detect import process_frame_for_line

# Create a basic robot
robot = Pitop()
drive = DriveController(left_motor_port="M3",
                        right_motor_port="M0")
robot.add_component(drive)
robot.add_component(PanTiltController(servo_pan_port="S0",
                                      servo_tilt_port="S3"))
robot.add_component(Camera(resolution=(640, 480),
                           format='PIL',
                           rotate_angle=0,
                           flip_top_bottom=True))
robot.pan_tilt.calibrate()


def process_new_camera_frame(camera_frame):
    line_data = process_frame_for_line(camera_frame)
    robot_view = line_data.robot_view
    center = line_data.line_center
    send_image(robot_view)

    if center is None:
        print(f"Line is lost!")
    else:
        x, y = center
        # COPY AND PASTE THE CODE YOU WROTE IN THE EXPLORATION SECTION
        if x

        elif x

        elif x


# SET THE SERVO ANGLES HERE
robot.pan_servo.target_angle =
robot.tilt_servo.target_angle =

robot.camera.on_frame = process_new_camera_frame

pause()