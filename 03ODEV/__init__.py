import cv2

def apply_histogram_equalization(image):

    equalized_image = cv2.equalizeHist(image)
    return equalized_image

if __name__ == "__main__":

    image_path = r'/images/kaplan.jpg'
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)


    if image is None:
        print("Error: Couldn't open or read the image.")
    else:

        equalized_image = apply_histogram_equalization(image)


        cv2.imshow('Original Image', image)
        cv2.imshow('Equalized Image', equalized_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()