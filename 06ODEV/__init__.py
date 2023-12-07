import cv2
import numpy as np
from matplotlib import pyplot as plt


image_path = r'C:\Users\yusuf\PycharmProjects\pythonProject\images\castle.jpg'
original_image = cv2.imread(image_path, cv2.IMREAD_COLOR)

if original_image is None:
    print("Error: Couldn't open or read the image.")
else:

    blurred_image = cv2.GaussianBlur(original_image, (3, 3), 0)


    gray_image = cv2.cvtColor(blurred_image, cv2.COLOR_BGR2GRAY)


    laplace_filtered_image = cv2.Laplacian(gray_image, cv2.CV_16S)


    laplace_filtered_image = cv2.convertScaleAbs(laplace_filtered_image)


    plt.figure(figsize=(8, 4))

    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(laplace_filtered_image, cmap='gray')
    plt.title('Sharpened Image (Laplace + Gaussian)')
    plt.axis('off')

    plt.show()