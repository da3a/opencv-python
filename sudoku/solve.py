
import cv2 as cv
import numpy as np
import letter_recog

#500x500
padding = 3
image = cv.imread("test2.jpg")[padding:-padding,padding:-padding]
height, width, channels = image.shape
cellW = width/9
cellH = height/9

gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
# gray = cv.GaussianBlur(gray, (11, 11), 0)
outerBox = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 5, 2)
outerBox = cv.bitwise_not(outerBox)

# cv.imshow('outerBox', outerBox)

y=0
x=3
box = outerBox[cellH*y + padding:cellH*(y+1) - padding, cellW*x + padding:cellW*(x+1) - padding]
# cv.imshow('box', box)

# res = letter_recog.recogDigit(box)
# print(res)

for i in range(0, 9):
	for j in range(0, 9):
		box = outerBox[cellH*i + padding:cellH*(i+1) - padding, cellW*j + padding:cellW*(j+1) - padding]
		res = letter_recog.recogDigit(box)
		print(res)
		# cv.imshow("box {0}".format(x+1), outerBox[cellH*x:cellH*(x+1), cellW*x:cellW*(x+1)])

cv.waitKey(0)
cv.destroyAllWindows()
