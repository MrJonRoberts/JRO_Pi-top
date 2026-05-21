# //////////////////////// LOCATE BLUE LINE ///////////////////////
from pitop import Pitop, DriveController, Camera, PanTiltController
from time import sleep
from further_link import send_image
from signal import pause
from pitop.processing.algorithms.line_detect import process_frame_for_line

# Create a basic robot
robot = Pitop()
drive = DriveController(left_motor_port="M3",
                        right_motor_port="M0")
robot.add_component(PanTiltController(servo_pan_port="S0",
                                      servo_tilt_port="S3"))
robot.add_component(drive)
robot.add_component(Camera(resolution=(640, 480),
                           format='PIL',
                           rotate_angle=0,
                           flip_top_bottom=True))


def process_new_camera_frame(camera_frame):
    # get data about the line from the camere image
    line_data = process_frame_for_line(camera_frame)

    # get what the robot sees from line data
    robot_view = line_data.robot_view

    # get the center of the blue line
    center = line_data.line_center

    # send the robot's view to Further so we can see it
    send_image(robot_view)

    if center is None:
        # if there is no line center calculated, then the line must be lost
        print(f"Line is lost!")
    else:
        # get x, y coordinates from the center value
        x, y = center

        # print to the console so we can view the data
        print(f'Center (x, y) of the line is:({x}, {y})')


robot.camera.on_frame = process_new_camera_frame

pause()