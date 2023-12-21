import cv2
import numpy as np
from matplotlib import pyplot as plt

def apply_gaussian_filter(image, kernel_size, sigma):
    blurred_image = cv2.GaussianBlur(image, (kernel_size, kernel_size), sigma)
    return blurred_image

if __name__ == "__main__":
    image_path = r'/images/zebra.jpg'
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if image is None:
        print("Error: Couldn't open or read the image.")
    else:
        blurred_image = apply_gaussian_filter(image, kernel_size=5, sigma=1)

        plt.figure(figsize=(8, 4))

        plt.subplot(1, 2, 1)
        plt.imshow(image, cmap='gray')
        plt.title('Original Image')
        plt.axis('off')

        plt.subplot(1, 2, 2)
        plt.imshow(blurred_image, cmap='gray')
        plt.axis('off')

        plt.show()