
import cv2
import numpy as np


def tuz_biber_ekle(img, salt_prob, pepper_prob):
    noisy = np.copy(img)


    num_salt = np.ceil(salt_prob * img.size)
    coords = [np.random.randint(0, i - 1, int(num_salt))
              for i in img.shape]
    noisy[coords] = 1

    coords = [np.random.randint(0, i - 1, int(pepper_prob))
              for i in img.shape]
    noisy[coords] = 0

    return noisy


def kontrahormon_temizle(img, kernel_size=(3, 3)):

    denoised = cv2.medianBlur(img, ksize=kernel_size)
    return denoised

image_path = r'/images/castle.jpg'

image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)


noisy_image = tuz_biber_ekle(image, salt_prob=0.02, pepper_prob=0.02)

denoised_image = kontrahormon_temizle(noisy_image)

cv2.imshow("Orjinal Resim", image)
cv2.imshow("Tuz-Biber Eklenmiş Resim", noisy_image)
cv2.imshow("Kontrahormon Temizlenmiş Resim", denoised_image)
cv2.waitKey(0)
cv2.destroyAllWindows()