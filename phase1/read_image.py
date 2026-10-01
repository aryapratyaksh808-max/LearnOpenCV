''' contains basic three function of opencv with absolute and relative url change image 1 to image to'''
import cv2
image = cv2.imread("C:/Users/lenovo/OneDrive/Desktop/ai/LearnOpenCV/images/hanuman_ji.jpg")#here i used the absolute path of the image
image2 = cv2.imread("../images/ss.jpg")# here i used relative url

if image2 is not None:
     print("image is loaded")
else:
     print("images is not loaded")
cv2.imshow("HANUMAN JI",image2)#images show function use to show any image
cv2.waitKey(0)#Show images unless we don't press any key
cv2.destroyAllWindows()#for closing all windows we have created to open 