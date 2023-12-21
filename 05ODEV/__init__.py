import cv2
import numpy as np

def adjust_gamma(image_path, gamma=1.0):
    original_image = cv2.imread(image_path)

    gamma_corrected = np.power(original_image / float(np.max(original_image)), gamma) * 255.0
    gamma_corrected = np.uint8(gamma_corrected)

    cv2.imshow('Original Image', original_image)
    cv2.imshow('Gamma Corrected Image', gamma_corrected)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image_path = r'/images/castle.jpg'

gamma_value = 1.5
adjust_gamma(image_path, gamma_value)