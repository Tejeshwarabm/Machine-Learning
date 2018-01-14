#! /usr/bin/env python

'''
Developed: 14-01-2018
	   Tejeshwara
	   NITK Surathkal, M.Tech - CSE
'''

# import the necessary packages
#from __future__ import print_function
import numpy as np
import argparse
import cv2
import glob
import os
import sys
from pythonds.basic.stack import Stack

count = 1
def adjust_gamma(image, gamma=1.0):
	# build a lookup table mapping the pixel values [0, 255] to
	# their adjusted gamma values
	invGamma = 1.0 / gamma
	table = np.array([((i / 255.0) ** invGamma) * 255
		for i in np.arange(0, 256)]).astype("uint8")
 
	# apply gamma correction using the lookup table
	return cv2.LUT(image, table)


def enhance_image(original):
	global count
	# loop over various values of gamma
	for gamma in np.arange(0.5, 3.5, 0.3):
		# ignore when gamma is 1 (there will be no change to the image)
		if gamma == 1:
			continue
	 
		# apply gamma correction and show the images
		gamma = gamma if gamma > 0 else 0.1
		adjusted = adjust_gamma(original, gamma=gamma)
		'''
		# It shows the gamma variance of the image
		cv2.putText(adjusted, "", (10, 30),
			cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
	
		cv2.putText(adjusted, "g={}".format(gamma), (10, 30),
			cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
	
		cv2.imshow("Images", np.hstack([original, adjusted]))
		cv2.waitKey(0)
		'''
		cv2.imwrite(str(count)+'.jpg',adjusted)
		count += 1
	return


def colorMap(original, count):
	'''
	# these are different values of color
		Value	Name	
	0	COLORMAP_AUTUMN	
	1	COLORMAP_BONE	
	2	COLORMAP_JET	
	3	COLORMAP_WINTER	
	4	COLORMAP_RAINBOW	
	5	COLORMAP_OCEAN	
	6	COLORMAP_SUMMER	
	7	COLORMAP_SPRING	
	8	COLORMAP_COOL	
	9	COLORMAP_HSV	
	10	COLORMAP_PINK	
	11	COLORMAP_HOT
	'''

	# color Maps are in the range between 0 to 11
	if (count >= 0) and (count <= 11): 
		#print count
		#gray = cv2.imread(original)
		color = cv2.applyColorMap(original, count)
		#cv2.imshow(str(count), np.hstack([gray,color]))
		#cv2.waitKey(0)
		
	else:
		print "count is not in range"
		
	return color

img = sys.argv[1]
print img
originial = cv2.imread(img)
s = Stack()
for i in range(12):
	colour = colorMap(originial,i)
	print i
	s.push(colour)

print "Completed"

#cv2.imshow("Image",np.hstack([original,img0, img1,img2,img3,img4,img5,img6,img7,img8,img9,img10,img11]))
cv2.imshow("Image: Real-- Hot - Pink - HSV - Cool - Spring - Summer",np.hstack([originial,s.pop(),s.pop(),s.pop(),s.pop(),s.pop(),s.pop()]))
cv2.waitKey(0)

cv2.imshow("Image: Real-- Ocean - Rainbow - Winter - Jet - Bone - Autumn",np.hstack([originial,s.pop(),s.pop(),s.pop(),s.pop(),s.pop(),s.pop()]))
cv2.waitKey(0)

'''

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
args = vars(ap.parse_args())

# load the original image
#original = cv2.imread(args["image"])

main_Dir = args["image"]
#main_Dir = sys.argv[1]
#print(main_Dir)
image_path = os.path.join(main_Dir,'*.jpg')
#print(image_path)

for name in glob.glob(image_path):
	print(name)
	#print("\n\n\n")
	original = cv2.imread(name)
	enhance_image(original)

print("Done......")

'''



