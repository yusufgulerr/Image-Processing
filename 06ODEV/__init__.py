import cv2
import numpy as np

def apply_average_filter(image_path, kernel_size=(5, 5)):

    original_image = cv2.imread(image_path)


    filtered_image = cv2.blur(original_image, kernel_size)


    cv2.imshow('Original Image', original_image)
    cv2.imshow('Average Filtered Image', filtered_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image_path = image_path = r'/images/kahve.jpg'


kernel_size = (5, 5)

apply_average_filter(image_path, kernel_size)