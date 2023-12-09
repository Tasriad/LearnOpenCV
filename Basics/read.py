import cv2 as cv
# reading images

# img = cv.imread('Photos/cat_large.jpg') # Read the image
# cv.imshow('Cat', img) # Show the image
# cv.waitKey(0)  # 0 means infinite time to wait for a key press
# point 1: large image is not shown completely

# reading videos

# capture = cv.VideoCapture('Videos/dog.mp4')

# while True:
#     isTrue, frame = capture.read() # isTrue is a boolean variable
#     cv.imshow('Video', frame) # frame is a numpy array
#     if cv.waitKey(20) & 0xFF == ord('d'): # if d is pressed, break the loop
#         break
    
# capture.release() # release the capture
# cv.destroyAllWindows() # destroy all the windows

# resize and rescale videos

# def rescaleFrame(frame, scale=0.75):
#     # images, videos and live videos
#     width = int(frame.shape[1]*scale) # shape[1] is the width
#     height = int(frame.shape[0]*scale) # shape[0] is the height
#     dimensions = (width, height)
#     return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# capture = cv.VideoCapture('Videos/dog.mp4')

# while True:
#     isTrue, frame = capture.read() # isTrue is a boolean variable
#     frame_resized = rescaleFrame(frame, scale=0.2)
#     cv.imshow('Video', frame) # frame is a numpy array
#     cv.imshow('Video Resized', frame_resized)
#     if cv.waitKey(20) & 0xFF == ord('d'): # if d is pressed, break the loop
#         break
    
# capture.release() # release the capture
# cv.destroyAllWindows() # destroy all the windows

# resize and rescale images

# img = cv.imread('Photos/cat_large.jpg') # Read the image
# cv.imshow('Cat', img) # Show the image
# cv.imshow('Cat Resized', rescaleFrame(img, scale=0.2))
# cv.waitKey(0)


