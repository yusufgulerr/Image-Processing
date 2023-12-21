import cv2
import numpy as np

def apply_blur_and_sharpen(image_path, kernel_size=(5, 5)):
    original_image = cv2.imread(image_path)

    blurred_image = cv2.GaussianBlur(original_image, kernel_size, 0)

    kernel = np.array([[-1, -1, -1],
                       [-1, 9, -1],
                       [-1, -1, -1]])

    sharpened_image = cv2.filter2D(blurred_image, -1, kernel)

    cv2.imshow('Original Image', original_image)
    cv2.imshow('Blurred Image', blurred_image)
    cv2.imshow('Sharpened Image', sharpened_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image = cv2.imread(r'/images/zebra.jpg')

kernel_size = (5, 5)

apply_blur_and_sharpen(image, kernel_size)