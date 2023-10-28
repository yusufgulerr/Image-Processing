import cv2
import os

image_directory = "image"
image_name = "kedi_resmi.jpg"

image_path = os.path.join(image_directory, image_name)


image = cv2.imread(image_path)
alpha = 1.5

result = cv2.convertScaleAbs(image, alpha=alpha, beta=0)


cv2.imshow("Original Image", image)
cv2.imshow("Contrast Enhanced Image", result)
cv2.waitKey(0)
cv2.destroyAllWindows()