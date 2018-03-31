import cv2
import aircv

img = cv2.imread("C:\\1.jpg")
cv2.imshow("lena",img)
#cv2.waitKey(10000)

img1 = cv2.imread("C:\\1.jpg")
crop_img = img1[300:400, 50:300]
cv2.imshow("image", crop_img)
cv2.waitKey(10000)


result=aircv.find_template(img,img1)

print(result["confidence"])