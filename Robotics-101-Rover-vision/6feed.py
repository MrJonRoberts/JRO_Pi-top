#/////////////// CONTINUOUS CAMERA FEED ////////////////
from pitop import Pitop, Camera
from time import sleep
from further_link import send_image
from signal import pause

# Create a basic robot
robot = Pitop()
robot.add_component(Camera(resolution=(640, 480),
                               format='PIL',
                               rotate_angle=0,
                               flip_top_bottom=True))

def camera_callback(camera_frame):
    send_image(camera_frame)

robot.camera.on_frame = camera_callback
pause()