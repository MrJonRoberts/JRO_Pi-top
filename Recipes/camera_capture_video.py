from pitop.camera import Camera
from time import sleep
from further_link import send_image

camera = Camera()

# Start recording video in the background
camera.start_video_capture('/home/pi/Desktop/video.avi')

# Wait 5 seconds for the camera to record some footage
sleep(5)

# Stop recording, the video will be saved in ~/Camera/
camera.stop_video_capture()