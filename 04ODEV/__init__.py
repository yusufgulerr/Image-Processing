import cv2
import numpy as np
from matplotlib import pyplot as plt

def apply_averaging_filter(image, filter_size):
    averaged_image = cv2.blur(image, (filter_size, filter_size))
    return averaged_image

def apply_box_filter(image, filter_size):
    # Create a box filter kernel
    kernel = np.ones((filter_size, filter_size), np.float32) / (filter_size * filter_size)

    box_filtered_image = cv2.filter2D(image, -1, kernel)
    return box_filtered_image

if __name__ == "__main__":
    image_path = r'C:\Users\yusuf\PycharmProjects\pythonProject\images\dag.jpg'
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if image is None:
        print("Error: Couldn't open or read the image.")
    else:
        averaged_image = apply_averaging_filter(image, filter_size=15)

        box_filtered_image = apply_box_filter(image, filter_size=15)

        plt.figure(figsize=(12, 4))

        plt.subplot(1, 3, 1)
        plt.imshow(image, cmap='gray')
        plt.title('Original Image')
        plt.axis('off')

        plt.subplot(1, 3, 2)
        plt.imshow(averaged_image, cmap='gray')
        plt.title('Averaging Filter (cv2.blur)')
        plt.axis('off')

        plt.subplot(1, 3, 3)
        plt.imshow(box_filtered_image, cmap='gray')
        plt.title('Box Filter (cv2.filter2D)')
        plt.axis('off')

        plt.show()