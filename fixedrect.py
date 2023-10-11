import cv2
import numpy as np

#RESOURCES USED
#https://docs.opencv.org/4.x/df/d9d/tutorial_py_colorspaces.html
#https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html
#https://docs.opencv.org/4.x/dd/d49/tutorial_py_contour_features.html
#https://code.likeagirl.io/finding-dominant-colour-on-an-image-b4e075f98097

def get_dominant_color(image, rect):
    x, y, w, h = rect
    roi = image[y:y + h, x:x + w]

    pixels = roi.reshape((-1, 3))

    pixels = np.float32(pixels)

    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
    k = 3  
    _, labels, centers = cv2.kmeans(pixels, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    dominant_color = np.uint8(centers[0])

    return dominant_color

def display_dominant_color(frame, dominant_color):
    color_block = np.zeros((100, 100, 3), dtype=np.uint8)
    color_block[:, :] = dominant_color

    frame[10:110, 10:110] = color_block

    cv2.imshow("Video Feed", frame)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    central_rect = (215, 150, 200, 200)

    dominant_color = get_dominant_color(frame, central_rect)

    display_dominant_color(frame, dominant_color)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()