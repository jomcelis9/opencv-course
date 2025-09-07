#pylint:disable=no-member

import cv2 as cv

# # READ IMAGES
# img = cv.imread('Resources/Photos/cat_large.jpg')
# cv.imshow('Cat',img)
# cv.waitKey(0)
# Mawalang galng

# RESIZE VIDEOS
def rescaleFrame(frame, scale = 0.75):
    
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# READ VIDEOS

capture = cv.VideoCapture('Resources/Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)
    cv.imshow('Video', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()




# # Read in an image
# img = cv.imread('../Resources/Photos/park.jpg')
# cv.imshow('Park', img)

# # Converting to grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# # Blur 
# blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

# # Edge Cascade
# canny = cv.Canny(blur, 125, 175)
# cv.imshow('Canny Edges', canny)

# # Dilating the image
# dilated = cv.dilate(canny, (7,7), iterations=3)
# cv.imshow('Dilated', dilated)

# # Eroding
# eroded = cv.erode(dilated, (7,7), iterations=3)
# cv.imshow('Eroded', eroded)

# # Resize
# resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
# cv.imshow('Resized', resized)

# # Cropping
# cropped = img[50:200, 200:400]
# cv.imshow('Cropped', cropped)