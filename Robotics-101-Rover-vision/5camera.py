#////////////// CAMERA FEEDBACK 100 FRAMES /////////////////
from pitop import Pitop, Camera
from time import sleep
from further_link import send_image

# Create a basic robot
robot = Pitop()
robot.add_component(Camera(resolution=(640, 480),
                               format='PIL',
                               rotate_angle=0,
                               flip_top_bottom=True))

for i in range(100):
    camera_frame = robot.camera.get_frame()
    print(f"Sending frame: {i}")
    send_image(camera_frame)