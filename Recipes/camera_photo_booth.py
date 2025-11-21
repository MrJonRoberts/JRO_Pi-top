from pitop.camera import Camera
from further_link import send_image
from time import sleep

# Set up the camera
camera = Camera()
# Send each camera frame to show in Further
camera.on_frame = send_image

# Count down from 5
for i in range(5, 0, -1):
    print(i)
    sleep(1)

print('Say cheese!')
sleep(1)

# Grab an image from the camera
image = camera.get_frame()
# Save the image to the Desktop
image.save('/home/pi/Desktop/picture.jpg')