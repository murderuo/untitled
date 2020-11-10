# import cv2
#
# g_image=cv2.imread("test.jpg",cv2.CV_LOAD_IMAGE_GRAYSCALE)
#
# cv2.imwrite("test_grey.png",g_image)

import cv2

img=cv2.imread("test.jpg",)

# print(cv2.__version__)
cv2.imshow("",img)
# cv2.imwrite("test.png",img) #save image "test.png" same folder
print(img.shape)
print(img.size)
# cv2.waitKey(0)
# cv2.destroyAllWindows()




