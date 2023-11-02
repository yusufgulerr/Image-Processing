import cv2
import numpy as np
from matplotlib import pyplot as plt

image_path = r'C:\Users\yusuf\PycharmProjects\pythonProject\images\kaplan.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: Couldn't open or read the image.")
else:
    # Perform contrast stretching
    min_intensity = np.min(image)
    max_intensity = np.max(image)

    # Linear contrast stretch formula
    stretched_image = 255 * ((image - min_intensity) / (max_intensity - min_intensity))

    # Convert the result back to uint8
    stretched_image = stretched_image.astype(np.uint8)

    # Display the original and stretched images
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.title('Original Image')
    plt.imshow(image, cmap='gray')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.title('Contrast Stretched Image')
    plt.imshow(stretched_image, cmap='gray')
    plt.axis('off')

    plt.show()