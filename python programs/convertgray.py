import cv2
import numpy as np

img = cv2.imread('images\p2.jpg',0)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
print ("ESCAPE TO QUIT OR S TO SAVE AND EXIT")
k = cv2.waitKey(0)
if k==27 :
     cv2.destroyAllWindows()
elif k== ord('s')  :
    cv2.imwrite('p1gray.png',img)
    destroyAllWindows
