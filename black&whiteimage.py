import cv2
import numpy as np

while True:
    img = cv2.imread('goku.jpg')
    final_img = np.array(img)
    cv2.imshow('Goku', final_img)

    # Converting Image to Grayscale
    gray = cv2.cvtColor(final_img, cv2.COLOR_RGB2GRAY)
    cv2.imshow('Goku', gray)
    cv2.imwrite("D:\SACHIN\GrayGoku.jpg", gray)


    if cv2.waitKey(10) == ord('q'):
        break
