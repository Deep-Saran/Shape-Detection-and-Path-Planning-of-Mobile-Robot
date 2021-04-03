import cv2
import numpy as np
import matplotlib.pyplot as plt
import __future__ import print_function
cap= cv2.VideoCapture(0)
ret, img = cap.read()
cap.release()

#img = cv2.imread('treee.JPG')


# cut out excessive parts of image here
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('frame',imgGray)
ret, thresh = cv2.threshold(imgGray, 127, 255, 0)
image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# which contour to use?

print(contours[56].size)#55
largest = 0
indexLargest = 0
for i in xrange(0, len(contours)):
    area = cv2.contourArea(contours[i])
    if area > largest:
        largest = area
        indexLargest = i
   # print "array value: %d  array size: %d contour area: %d"% (i,contours[i].size,area)
largestContour = contours.pop(indexLargest)
secondLargest = 0
indexSecondLargest = 0
for i in xrange(0, len(contours)):
    area = cv2.contourArea(contours[i])
    if area > secondLargest:
        secondLargest = area
        indexSecondLargest = i
    #print "array value: %d  array size: %d contour area: %d"% (i,contours[i].size,area)

contourArray = contours[indexSecondLargest]#46
print "second largest index: %d  "% (indexSecondLargest)
cArray = contourArray[:, 0]
x = cArray[:, 0]
for point in x:
    print "%d ," % (point)
#print(x)

print("y array/n")

y = cArray[:, 1]
#print(y)
for point in y:
    s= str("%d, ")
    print_function( s, end = '')
plt.plot(x, y)
plt.show()

