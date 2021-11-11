import cv2
import numpy as np

geohash = []

img = cv2.imread("way.png", 1)

print(img.shape)
arr = np.asarray(img,np.uint8)

print(type(img[150,150]))

for i in range(200):
    for a in range(200):
        if np.any(img[i, a] == 0):
            geohash.append("R"+str(i)+str(a)+"B")
        elif np.any(img[i, a] != 0):
            geohash.append("R"+str(i)+str(a))

print(geohash)




cv2.imshow("image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()


