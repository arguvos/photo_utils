import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import sys

if len(sys.argv) != 2:
	print("ERROR: Util expected path to images as a argument")
	sys.exit()

path = sys.argv[1]
print("Files and directories in '", path, "':")

dir_list = os.listdir(path)
print(dir_list)

for x in dir_list:
	print(x)
	image = cv2.imread(path + x)

	#seperating colour channels
	B = image[:,:,0] #blue layer
	G = image[:,:,1] #green layer
	R = image[:,:,2] #red layer

	#equilize each channel seperately
	b_equi = cv2.equalizeHist(B)
	g_equi = cv2.equalizeHist(G)
	r_equi = cv2.equalizeHist(R)
	
	#merge thechannels and create new image
	equi_im = cv2.merge([b_equi,g_equi,r_equi])

	cv2.imwrite(path + "out_" + x, equi_im)