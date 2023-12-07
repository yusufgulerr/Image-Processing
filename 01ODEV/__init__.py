import cv2
import numpy as np

def intensity_slicing(image_path, lower_threshold, upper_threshold):

    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    mask = cv2.inRange(img, lower_threshold, upper_threshold)
    result = cv2.bitwise_and(img, img, mask=mask)


    cv2.imshow('Original Image', img)
    cv2.imshow('Intensity Sliced Image', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


image_path = r'C:\Users\yusuf\PycharmProjects\pythonProject\images\kahve.jpg'
lower_threshold = 100
upper_threshold = 200

intensity_slicing(image_path, lower_threshold, upper_threshold)