import cv2
import numpy as np

img = cv2.imread('images/p9.png',0)
img = cv2.medianBlur(img,5)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
font = cv2.FONT_HERSHEY_SIMPLEX

circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,param1=35,param2=25,minRadius=10,maxRadius=100)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
    print(str(i[2]))
    #cv2.putText(img,'i[2]',(i[0],i[1]), font, 4,(255,255,0),2,cv2.LINE_AA)

cv2.imshow('detected circles',cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
