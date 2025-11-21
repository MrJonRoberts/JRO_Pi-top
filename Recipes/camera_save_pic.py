from pitop.camera import Camera
# Set up the camera
camera = Camera()
# Grab an image from the camera
image = camera.get_frame()
# Save the image to the Desktop
image.save('~/Desktop/picture.jpg')