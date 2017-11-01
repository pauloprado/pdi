import os
import cv2
import math
import argparse
import bob.measure
import numpy as np
from sklearn import metrics
import matplotlib.pyplot as plt
import Utils

# Hold the eer (Equal error rate) for each index
eers = []

# Argument parsing
parser = argparse.ArgumentParser(description='Extract vegetation indexes.')
parser.add_argument('-i', action='store', dest='inputList')
parser.add_argument('-f', action='store', dest='filterType')
parser.add_argument('-o', action='store', dest='outputDir')
args = parser.parse_args()

'''
	Plot the ROC curve and calculate the AUC, ERR, FAR and FRR
	@param label The ground truth
	@param targets List of arrays with the index value of each pixel
	@param labels Label of each curve that will be plotted
'''
def plot_roc(label, target, labels, fusion):
	print("\n-------------\n|Method|AUC|EER|FAR|FRR|Accuracy|")
	print("|:----------:|:-------------:|:------:|:------:|:------:|:------:|")
	# Use SKLearn to get the False Positive Rate (fpr), True Positive Rate(tpr)
	fpr, tpr, thresholds = metrics.roc_curve(label, target)

	print("%.3f" % metrics.roc_auc_score(label, target),end='')

	# Build an array where positive class will the their values, but the negative class will receive -1
	pos = np.where(label, target, -1)
	# Get position of all positive pixel (the position that isnt -1 value)
	posPos = np.where(pos>-1)
	# Build the array with only the values of positive class
	posVec = [target[i] for i in posPos]

	''' The same as the previous, but now for the negative class '''
	neg = np.where(1-label, target, -1)
	negPos = np.where(neg>-1)
	negVec = [target[i] for i in negPos]
	
	# Use the Bob package from IDIAP
	# Get the err value (Value where the False Acceptance Rate and the False Rejection Rate are equal)
	eer = bob.measure.eer_threshold(negVec[0].astype(np.double), posVec[0].astype(np.double))
	far, frr = bob.measure.farfrr(negVec[0].astype(np.double), posVec[0].astype(np.double), eer)
	eers.append(eer)

	prediction = np.where(target >= eer, 1, 0)
	acc = metrics.accuracy_score(label, prediction)

	print("|"+"%.3f" % eer+"|"+"%.3f" % far+"|"+"%.3f" % frr+"|"+"%.3f" % acc+"|")


	# plt.legend()
	# plt.xlabel("False Positive Rate - FPR")
	# plt.ylabel("True Positive Rate - TPR")
	# # plt.show()
	# plt.savefig(Utils.buildFileName(filterType, fusion, args.outputDir))
	# plt.clf()
'''
	
'''
def process(imgs):
	indices = [np.array([])]*6
	for i in imgs:
		indexes = []
		# Read original image and the ground truth
		img = cv2.blur(cv2.imread(i[0], cv2.IMREAD_COLOR),(5,5))
		gt = cv2.imread(i[1], cv2.IMREAD_GRAYSCALE)

		# Normalize the ground truth
		cv2.normalize(gt, gt, 0.0, 1.0, cv2.NORM_MINMAX)

		# Separate each channel
		B, G, R = cv2.split(np.float32(img))

		# NGRDI
		NGRDI = Utils.div0((G-R),(G+R))
		cv2.normalize(NGRDI, NGRDI, 0.0, 1.0, cv2.NORM_MINMAX)
		# cv2.normalize(NGRDI, NGRDI, 0.0, 255.0, cv2.NORM_MINMAX)
		# NGRDI = np.uint8(NGRDI)
		# cv2.imwrite("NGRDI.jpg", NGRDI)

		plot_roc(gt.ravel(), NGRDI.ravel(), Utils.idxsLabels, "noFusion")


def main():
	with open(args.inputList, 'r') as file:
		lines = file.readlines()
		imgs = []
		for line in lines:
			imgs.append(line.rstrip().split(' '))
	process(imgs)
if __name__=='__main__':
	main()


