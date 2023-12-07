import cv2
import numpy as np
from matplotlib import pyplot as plt


image = cv2.imread(r'C:\Users\yusuf\PycharmProjects\pythonProject\images\zebra.jpg')

lower_blue = np.array([100, 0, 0], dtype=np.uint8)
upper_blue = np.array([140, 255, 255], dtype=np.uint8)

mask = cv2.inRange(image, lower_blue, upper_blue)


segmented_image = cv2.bitwise_and(image, image, mask=mask)

# Orjinal ve bölütleme sonrası resimleri görselleştir
plt.subplot(131), plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)), plt.title('Original Image')
plt.subplot(132), plt.imshow(mask, cmap='gray'), plt.title('Mask')
plt.subplot(133), plt.imshow(cv2.cvtColor(segmented_image, cv2.COLOR_BGR2RGB)), plt.title('Segmented Image')
plt.show()