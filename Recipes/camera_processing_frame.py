from PIL import ImageDraw

from pitop import Camera

cam = Camera()


def draw_red_cross_over_image(im):
    # Use Pillow to draw a red cross over the image
    draw = ImageDraw.Draw(im)
    draw.line((0, 0) + im.size, fill=128, width=5)
    draw.line((0, im.size[1], im.size[0], 0), fill=128, width=5)
    return im


im = draw_red_cross_over_image(cam.get_frame())
im.show()


from time import sleep

import cv2

from pitop import Camera

cam = Camera(format="OpenCV")


def show_gray_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame", gray)
    cv2.waitKey(1)  # Necessary to show image


# Use callback function for 60s
cam.on_frame = show_gray_image
sleep(60)


# Use get_frame indefinitely
try:
    while True:
        show_gray_image(cam.get_frame())

except KeyboardInterrupt:
    cv2.destroyAllWindows()