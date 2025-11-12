from time import sleep

from pitop import Camera

# Record a 10s video to ~/Camera/

cam = Camera()

cam.start_video_capture()
sleep(10)
cam.stop_video_capture()


from pitop import Camera

c = Camera()
c.format = "OpenCV"


from pitop import Camera

c = Camera(format="OpenCV")


from pitop import Camera

cam = Camera()

while True:
    image = cam.get_frame()
    print(image.getpixel((0, 0)))



from time import sleep

from pitop import Camera

# Record a 10s video to ~/Camera/

cam = Camera()

cam.start_video_capture()
sleep(10)
cam.stop_video_capture()