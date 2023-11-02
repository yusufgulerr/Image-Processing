import cv2

def apply_histogram_equalization(image):
    # Apply histogram equalization
    equalized_image = cv2.equalizeHist(image)
    return equalized_image

if __name__ == "__main__":
    # Load the image
    image_path = r'C:\Users\yusuf\PycharmProjects\pythonProject\images\tepe.jpg'
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Check if the image was successfully loaded
    if image is None:
        print("Error: Couldn't open or read the image.")
    else:
        # Apply histogram equalization
        equalized_image = apply_histogram_equalization(image)

        # Display the original and equalized images
        cv2.imshow('Original Image', image)
        cv2.imshow('Equalized Image', equalized_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()