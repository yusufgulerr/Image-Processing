import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image
image_path = r'C:\Users\yusuf\PycharmProjects\pythonProject\images\castle.jpg'
original_image = cv2.imread(image_path, cv2.IMREAD_COLOR)

# Check if the image was successfully loaded
if original_image is None:
    print("Error: Couldn't open or read the image.")
else:
    # Reduce noise by blurring with a Gaussian filter
    blurred_image = cv2.GaussianBlur(original_image, (3, 3), 0)

    # Convert to gray
    gray_image = cv2.cvtColor(blurred_image, cv2.COLOR_BGR2GRAY)

    # Apply Laplace function
    laplace_filtered_image = cv2.Laplacian(gray_image, cv2.CV_16S)

    # Convert back to uint8
    laplace_filtered_image = cv2.convertScaleAbs(laplace_filtered_image)

    # Display the original and sharpened images
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