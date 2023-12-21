import cv2

def apply_gaussian_blur(image_path, kernel_size=(5, 5)):
    original_image = cv2.imread(image_path)

    blurred_image = cv2.GaussianBlur(original_image, kernel_size, 0)

    cv2.imshow('Original Image', original_image)
    cv2.imshow('Gaussian Blurred Image', blurred_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image = cv2.imread(r'/images/zebra.jpg')

kernel_size = (5, 5)

apply_gaussian_blur(image, kernel_size)