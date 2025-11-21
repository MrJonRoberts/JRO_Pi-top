import cv2
from pitop.camera import Camera
from further_link import send_image

# Set up our classifier from the xml data file
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

camera = Camera()
# Set the camera format to 'OpenCV' so the images can be processed
camera.format = 'OpenCV'

# Define a function to find faces in an image
def find_faces(image):
    # Convert the image to black and white
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Use the classifier to find faces
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        # Draw a rectangle around each face
        image = cv2.rectangle(image.copy(),(x,y),(x+w,y+h),(255,0,0),2)
    return image

# Start an infinite loop to generate images repeatedly
while True:
    # Grab a camera image
    frame = camera.get_frame()
    # Annotate the faces in the image
    frame = find_faces(frame)
    # Send the image to Further for display
    send_image(frame)