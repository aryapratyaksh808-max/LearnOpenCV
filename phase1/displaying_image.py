import cv2
image = cv2.imread("../images/hanuman_ji.jpg")
if image is not None:
     cv2.imshow("Hanuman ji image",image)
     cv2.waitKey(0)
     cv2.destroyAllWindows()
else:
     print("Not loaded")
