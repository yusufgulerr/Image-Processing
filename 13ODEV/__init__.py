import cv2
import numpy as np

def apply_contraharmonic_mean_filter(image_path, kernel_size=(3, 3), Q=1.5):
    original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    filtered_image = cv2.filter2D(original_image, -1, kernel=np.ones(kernel_size, np.float32) / (kernel_size[0] * kernel_size[1]), borderType=cv2.BORDER_CONSTANT)
    filtered_image = (original_image**(Q+1) - filtered_image**(Q+1)) / (original_image**Q - filtered_image**Q)

    filtered_image = np.uint8(filtered_image)

    cv2.imshow('Original Image', original_image)
    cv2.imshow('Contraharmonic Mean Filtered Image', filtered_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img_path = cv2.imread(r'/images/castle.jpg', 0)

kernel_size = (3, 3)

Q = 1.5

apply_contraharmonic_mean_filter(img_path, kernel_size, Q)