import cv2
image1 = cv2.imread("../images/hanuman_ji.jpg")
if image1 is not None:
     print("loaded")
     print("saving image...")
     cv2.imwrite("../images/hanuman_ji_copy.jpg",image1)
     print("image saved")
else: 
     print("not loaded")


