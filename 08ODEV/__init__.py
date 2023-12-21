import cv2
import numpy as np

def apply_sobel_filter(image_path):
    original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    sobel_x = cv2.Sobel(original_image, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(original_image, cv2.CV_64F, 0, 1, ksize=3)

    sobel_x = np.uint8(np.absolute(sobel_x))
    sobel_y = np.uint8(np.absolute(sobel_y))
    sobel_combined = cv2.bitwise_or(sobel_x, sobel_y)

    cv2.imshow('Original Image', original_image)
    cv2.imshow('Sobel Filtered Image', sobel_combined)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image_path = r'/images/castle.jpg'

apply_sobel_filter(image_path)