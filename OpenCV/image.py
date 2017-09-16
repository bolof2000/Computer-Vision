import cv2

img = cv2.imread("image.png",0)

cv2.waitKey(2000)
cv2.destroyAllWindows()
resize_image= cv2.resize(img,(1000,500))
cv2.imshow("show_image",resize_image)
cv2.imwrite("bolof.png",resize_image)
