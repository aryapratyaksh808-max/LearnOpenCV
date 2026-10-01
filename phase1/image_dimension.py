import cv2
image = cv2.imread("../images/hanuman_ji.jpg")
if image is not None:
    height, width = image.shape[:2]
    print(f"Image dimensions: {width} x {height}")