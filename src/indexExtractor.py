import os
import cv2
import argparse
import numpy as np

idxs = ['NGRDI', 'ExG', 'CIVE', 'VEG', 'ExGR', 'WI']

parser = argparse.ArgumentParser(description='Extract vegetation indexes.')
parser.add_argument('-i', action='store', dest='inputList')
# parser.add_argument('-o', action='store', dest='output')

args = parser.parse_args()

def div0( a, b ):
    with np.errstate(divide='ignore', invalid='ignore'):
        c = np.true_divide( a, b )
        c[ ~ np.isfinite( c )] = 0 
    return c

def process(imgs):
	for i in imgs:
		img = cv2.imread(i[0], cv2.IMREAD_COLOR)
		gt = cv2.imread(i[1], cv2.IMREAD_GRAYSCALE)
		cv2.normalize(gt, gt, 0.0, 1.0, cv2.NORM_MINMAX)

		B, G, R = cv2.split(np.float32(img))
		b = div0(B,(B+G+R))
		g = div0(G,(B+G+R))
		r = div0(R,(B+G+R))

		# NGRDI
		NGRDI = div0((G-R),(G+R))
		cv2.normalize(NGRDI, NGRDI, 0.0, 1.0, cv2.NORM_MINMAX)

		# ExG
		ExG = 2*g-r-b
		cv2.normalize(ExG, ExG, 0.0, 1.0, cv2.NORM_MINMAX)

		# CIVE
		CIVE = 0.411*r - 0.881*g + 0.385*b + 18.78745
		cv2.normalize(CIVE, CIVE, 0.0, 1.0, cv2.NORM_MINMAX)

		# VEG
		VEG = div0(g, (r**0.667)*(b**(1-0.667)))
		cv2.normalize(VEG, VEG, 0.0, 1.0, cv2.NORM_MINMAX)

		# ExGR
		ExGR = g-(2.4*r)-b # OK?
		cv2.normalize(ExGR, ExGR, 0.0, 1.0, cv2.NORM_MINMAX)

		# WI
		WI = div0((g-b),(r-g))
		cv2.normalize(WI, WI, 0.0, 1.0, cv2.NORM_MINMAX)



def main():
	with open(args.inputList, 'r') as file:
		lines = file.readlines()
		imgs = []
		for line in lines:
			imgs.append(line.rstrip().split(' '))
	process(imgs)
if __name__=='__main__':
	main()

