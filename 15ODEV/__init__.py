import cv2
import numpy as np

def opening_closing_operations(image_path, kernel_size=5):
    original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    kernel = np.ones((kernel_size, kernel_size), np.uint8)

    opened_image = cv2.morphologyEx(original_image, cv2.MORPH_OPEN, kernel)

    closed_image = cv2.morphologyEx(original_image, cv2.MORPH_CLOSE, kernel)

    cv2.imshow('Original Image', original_image)
    cv2.imshow('Opened Image', opened_image)
    cv2.imshow('Closed Image', closed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img_path = cv2.imread(r'/images/view.jpg', 0)

kernel_size = 5

opening_closing_operations(img_path, kernel_size)