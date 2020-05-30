#Import necessary libraries
import numpy as np
import pandas as pd
import cv2
import argparse

#Get Input image from the user using CommandPrompt/Terminal
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required = True, help = "Image Path")
args = vars(ap.parse_args())
img_path = args['image']

#Read with opencv
img = cv2.imread(img_path)
imgWidth = img.shape[1] - 40

#declaring global variables (are used later on)
r = g = b = xpos = ypos = 0

#Read the color dataset
index = ['color', 'color_name', 'hex', 'R', 'G', 'B']
data = pd.read_csv('colors.csv', names = index, header = None)


def getColorName(R,G,B):
	minimum = 10000
	for i in range(len(data)):
		d = abs(R - int(data.loc[i,"R"])) + abs(G - int(data.loc[i,"G"])) + abs(B - int(data.loc[i,"B"]))
		if (d <= minimum):
			minimum = d
			cname = data.loc[i, 'color_name'] + '   Hex=' + data.loc[i, 'hex']
	return cname


def identify_color(event, x, y, flags, param):
	global b, g, r, xpos, ypos, clicked
	xpos = x
	ypos = y
	b, g, r = img[y,x]
	b = int(b)
	g = int(g)
	r = int(r)


cv2.namedWindow('image')
cv2.setMouseCallback('image', identify_color)

while(1):
	cv2.imshow('image',img)
	cv2.rectangle(img,(20,20), (imgWidth,60), (b,g,r), -1)

	text = getColorName(r,g,b) + '   R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)
	#cv2.putText(img,text,start,font(0-7), fontScale, color, thickness, lineType, (optional bottomLeft bool) )
	cv2.putText(img, text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)
	#For very light colours we will display text in black colour
	if(r+g+b >= 600):
		cv2.putText(img, text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)

	if cv2.waitKey(20) & 0xFF == 27:
		break

cv2.destroyAllWindows()










