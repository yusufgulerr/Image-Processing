import cv2
import numpy as np

def segment_image(image_path):
    original_image = cv2.imread(image_path)

    image_rgb = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)

    lower_bound = np.array([50, 50, 50])
    upper_bound = np.array([150, 150, 150])

    mask = cv2.inRange(image_rgb, lower_bound, upper_bound)

    segmented_image = cv2.bitwise_and(original_image, original_image, mask=mask)

    cv2.imshow('Original Image', original_image)
    cv2.imshow('Segmented Image', segmented_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img_path = cv2.imread(r'/images/castle.jpg', 0)

segment_image(img_path)