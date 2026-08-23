import cv2
import matplotlib.pyplot as plt
import numpy as np

# Load image
img = cv2.imread('/content/space.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('/content/charliechaplin.jpg', cv2.IMREAD_GRAYSCALE)

def show_comparison(original, blur3, blur5, blur7):
    plt.figure(figsize=(12, 10))

    # Original
    plt.subplot(2,2,1)
    plt.imshow(original, cmap='gray')
    plt.title("Original Grayscale Image")
    plt.axis('off')

    # 3x3
    plt.subplot(2,2,2)
    plt.imshow(blur3, cmap='gray')
    plt.title("Average Filter (3×3)")
    plt.axis('off')

    # 5x5
    plt.subplot(2,2,3)
    plt.imshow(blur5, cmap='gray')
    plt.title("Average Filter (5×5)")
    plt.axis('off')

    # 7x7
    plt.subplot(2,2,4)
    plt.imshow(blur7, cmap='gray')
    plt.title("Average Filter (7×7)")
    plt.axis('off')

    plt.tight_layout()
    plt.show()


if img is None:
    print("Error: Image not found. Check the image path.")

elif img2 is None:
    print("Error: Image not found. Check the image path.")

else:

    # Select only ONE Charlie Chaplin image
    h, w = img2.shape
    img2 = img2[0:h//2, 0:w//2]

    # Correct average kernels
    kernel_3x3 = np.ones((3,3), np.float32) / 9
    kernel_5x5 = np.ones((5,5), np.float32) / 25
    kernel_7x7 = np.ones((7,7), np.float32) / 49

    # Apply filters to Space image
    blur_3x3 = cv2.filter2D(img, -1, kernel_3x3)
    blur_5x5 = cv2.filter2D(img, -1, kernel_5x5)
    blur_7x7 = cv2.filter2D(img, -1, kernel_7x7)

    show_comparison(img, blur_3x3, blur_5x5, blur_7x7)

    # Apply filters to Charlie Chaplin image
    blur_3x3 = cv2.filter2D(img2, -1, kernel_3x3)
    blur_5x5 = cv2.filter2D(img2, -1, kernel_5x5)
    blur_7x7 = cv2.filter2D(img2, -1, kernel_7x7)

    show_comparison(img2, blur_3x3, blur_5x5, blur_7x7)
