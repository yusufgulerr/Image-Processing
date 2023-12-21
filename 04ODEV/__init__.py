import cv2
import numpy as np

def contrast_stretching(image_path):
    original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    min_intensity = 50
    max_intensity = 200

    stretched_image = np.clip((original_image - original_image.min()) * ((max_intensity - min_intensity) / (original_image.max() - original_image.min())) + min_intensity, min_intensity, max_intensity).astype(np.uint8)

    cv2.imshow('Original Image', original_image)
    cv2.imshow('Contrast Stretched Image', stretched_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image_path = r'/images/dag.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)