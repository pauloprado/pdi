import os
import cv2
import math
import argparse
import bob.measure
import numpy as np
from sklearn import metrics
import matplotlib.pyplot as plt
import Utils

from joblib import Parallel, delayed
import multiprocessing

# Hold the eer (Equal error rate) for each index
eers = []

# Argument parsing
parser = argparse.ArgumentParser(description='Extract vegetation indexes.')
parser.add_argument('-i', action='store', dest='inputList')
parser.add_argument('-f', action='store', dest='filterType')
parser.add_argument('-o', action='store', dest='outputDir')
args = parser.parse_args()

filterType = 0

def parallel(j, pos, indP, indF):
	if(j in pos[0]):
		indP[j]=1
		indF[j]=0
	else:
		indP[j]=0
		indF[j]=1

def balanced_accuracy(label, predicted):
    k = [0,1]
    E = [None]*2
    for i in range(0,2):
        pos = np.where(label==k[i])
        indP = [None]*label.shape[0]
        indF = [None]*label.shape[0]

        num_cores = multiprocessing.cpu_count()
        Parallel(n_jobs=num_cores)(delayed(parallel)(i, pos, indP, indF) for i in range(0,label.shape[0]))
        # for j in range(0,label.shape[0]):
        #     if(j%10000 == 0):
        #         print(j)
        #     if(j in pos[0]):
        #         indP[j]=1
        #         indF[j]=0
        #     else:
        #         indP[j]=0
                # indF[j]=1
        
        Nc = len(np.where(label == k[i])[0])
        
        a=[]
        print("len "+len(indF))
        for j in range(0,len(indF)):
            if(indF[j] == 1):
                a.append(j)
        posVec = [predicted[j] for j in a]

        FP = 0
        for j in range(0, len(a)):
            if(predicted[a[j]] == k[i]):
                FP = FP+1
        e1 = float(FP)/(label.shape[0] - Nc)
        
        b=[]
        for j in range(0,len(indP)):
            if(indP[j] == 1):
                b.append(j)
        posVec = [predicted[j] for j in b]

        FN = 0
        for j in range(0, len(b)):
            if(predicted[b[j]] != k[i]):
                FN = FN+1
        
        e2 = float(FN)/Nc
        
        E[i] = e1+e2
    return 1 - sum(E)/4

'''
	Calculate the accuracy
	@param label The ground truth
	@param targets List of arrays with the prediction of each pixel
'''
def accuracy_late(label, targets):
	i = 0
	print("\n-------------\n|Method|Accuracy|\n|:----------:|:-------------:|")
	for target in targets:
		print("|"+Utils.lateFusionLabels[i]+"|"+"%.3f" % metrics.accuracy_score(label, target)+"|")
		i += 1

'''
	Plot the ROC curve and calculate the AUC, ERR, FAR and FRR
	@param label The ground truth
	@param targets List of arrays with the index value of each pixel
	@param labels Label of each curve that will be plotted
'''
def plot_roc(label, targets, labels, fusion):
	i = 0
	print("\n-------------\n|Method|AUC|EER|FAR|FRR|Accuracy|")
	print("|:----------:|:-------------:|:------:|:------:|:------:|:------:|")
	for target in targets:
		# if(np.any(np.isnan(target))):
		target[ ~ np.isfinite( target )] = 0
		# target[ ~ np.isnan( target )] = 0
		# Use SKLearn to get the False Positive Rate (fpr), True Positive Rate(tpr)
		fpr, tpr, thresholds = metrics.roc_curve(label, target)

		print("|"+labels[i]+"|"+"%.3f" % metrics.roc_auc_score(label, target),end='')

		# Plot the FPR vs TPR (ROC curve)
		plt.plot(fpr[::200], tpr[::200], lw=2, label=labels[i])
		# Plot the straight to show the EER point
		plt.plot(np.array((1.00,0)), np.array((0,1.00)))
		i += 1

		# Build an array where positive class will the their values, but the negative class will receive -1
		pos = np.where(label, target, -1)
		# Get position of all positive pixel (the position that isnt -1 value)
		posPos = np.where(pos>-1)
		# Build the array with only the values of positive class
		posVec = [target[j] for j in posPos]

		''' The same as the previous, but now for the negative class '''
		neg = np.where(1-label, target, -1)
		negPos = np.where(neg>-1)
		negVec = [target[j] for j in negPos]
		
		# Use the Bob package from IDIAP
		# Get the err value (Value where the False Acceptance Rate and the False Rejection Rate are equal)
		eer = bob.measure.eer_threshold(negVec[0], posVec[0])
		far, frr = bob.measure.farfrr(negVec[0], posVec[0], eer)
		eers.append(eer)

		prediction = np.where(target >= eer, 1, 0)
		acc = metrics.balanced_accuracy_score(label, prediction)

		print("|"+"%.3f" % eer+"|"+"%.3f" % far+"|"+"%.3f" % frr+"|"+"%.3f" % acc+"|")


	plt.legend()
	plt.xlabel("False Positive Rate - FPR")
	plt.ylabel("True Positive Rate - TPR")
	# plt.show()
	plt.savefig(Utils.buildFileName(filterType, fusion, args.outputDir))
	plt.clf()

'''
	Do the processing for the early fusion methods, which are the Arithmetic mean and the Geometric mean
	@param label The ground truth, just pass forward in function call sequence
	@param indices The value of each pixel for all the indeces
'''
def early_fusion(label, indices):
	early_fusion_results = []
	# Mean
	mean = indices[0]
	for i in range(1,len(indices),1):
		mean = (mean + indices[i])
	mean = mean/len(indices)
	early_fusion_results.append(mean)
	
	# Geometric mean
	# P = produtorio(P(i)[x,y])/(produtorio(P(i)[x,y]) + produtorio(1-P(i)))
	geometricMean = indices[0]
	geometricMeanRenorm = 1 - indices[0]
	for i in range(1,len(indices),1):
		geometricMean = geometricMean*indices[i]
		geometricMeanRenorm = geometricMeanRenorm*(1-indices[i])
	geometricMean = geometricMean/(geometricMean + geometricMeanRenorm)
	early_fusion_results.append(geometricMean)

	plot_roc(label, early_fusion_results, Utils.earlyFusonLabels, "earlyFusion")

'''
	Do the processing for the late fusion method, which is the majority voting
	@param label The ground truth, just pass forward in function call sequence
	@param indices The value of each pixel for all the indeces
'''
def late_fusion(label, indices):
	i = 0
	late_fusion_results = []
	indicesThresholdeds = []
	for indice in indices:
		# Where the value of the prediction is greater or equal to EER value of that indice, 1 otherwise 0
		indicesThresholdeds.append(np.where(indice >= eers[i], 1, 0))
		i += 1

	# Sum all the value
	for idx in range(1, len(indicesThresholdeds)):
		indicesThresholdeds[0] = np.add(indicesThresholdeds[0], indicesThresholdeds[idx])
	
	# Where the sum of the 1's is greater than half of the indices, mean that this prediction has the majority of the votes
	late_fusion_results.append(np.where(indicesThresholdeds[0] >= math.floor(len(Utils.idxsLabels)/2)+1, 1, 0).astype(float))
	accuracy_late(label, late_fusion_results)

def filterImg(imgPath):
	global filterType
	img = cv2.imread(imgPath, cv2.IMREAD_COLOR)

	if filterType == 0: # No filter
		return img
	elif filterType == 1: # Normal blur
		return cv2.blur(img,(5,5))
	elif filterType == 2: # Gaussian blur
		return cv2.GaussianBlur(img,(5,5),0)
	elif filterType == 3: # Median blur
		return cv2.medianBlur(img,5)
	elif filterType == 4: # Bilateral filter
		return cv2.bilateralFilter(img,3,25,75) #src,dst,d,sigmaColor,sigmaSpace; | sigmaColor High sigmaColor mean that father color well be mixed together


'''
	
'''
def process(imgs):
	gtAllImgs = np.array([])
	indices = [np.array([])]*6
	for i in imgs:
		indexes = []

		# Read original image and the ground truth
		img = filterImg(i[0])
		gt = cv2.imread(i[1], cv2.IMREAD_GRAYSCALE)

		y,x = gt.shape
		if(img.shape != gt.shape):
			y, x = gt.shape
			img = img[0:y,0:x,]
		
		# Normalize the ground truth
		cv2.normalize(gt, gt, 0.0, 1.0, cv2.NORM_MINMAX)
		# Build a vector with all the ground truths
		gtAllImgs = np.concatenate((gtAllImgs, gt.ravel()))

		# Separate each channel
		B, G, R = cv2.split(np.float32(img))
		b = Utils.div0(B,(B+G+R))
		g = Utils.div0(G,(B+G+R))
		r = Utils.div0(R,(B+G+R))

		# NGRDI
		NGRDI = Utils.div0((G-R),(G+R))
		cv2.normalize(NGRDI, NGRDI, 0.0, 1.0, cv2.NORM_MINMAX)
		indices[0] = np.concatenate((indices[0], NGRDI.ravel()))
		# cv2.normalize(NGRDI, NGRDI, 0.0, 255.0, cv2.NORM_MINMAX)
		# NGRDI = np.uint8(NGRDI)
		# cv2.imwrite("NGRDI.jpg", NGRDI)

		# ExG
		# ExG = 2*gNorm-rNorm-bNorm
		ExG = 2*g-r-b
		cv2.normalize(ExG, ExG, 0.0, 1.0, cv2.NORM_MINMAX)
		indices[1] = np.concatenate((indices[1], ExG.ravel()))
		# cv2.normalize(ExG, ExG, 0.0, 255.0, cv2.NORM_MINMAX)
		# ExG = np.uint8(ExG)
		# cv2.imwrite("ExG.jpg", ExG)

		# CIVE
		CIVE = 0.411*R - 0.881*G + 0.385*B + 18.78745
		CIVE = 1 - cv2.normalize(CIVE, CIVE, 0.0, 1.0, cv2.NORM_MINMAX)
		indices[2] = np.concatenate((indices[2], CIVE.ravel()))
		# cv2.normalize(CIVE, CIVE, 0.0, 255.0, cv2.NORM_MINMAX)
		# CIVE = np.uint8(CIVE)
		# cv2.imwrite("CIVE.jpg", CIVE)

		# VEG
		VEG = Utils.div0(g, 2+(r**0.667)*(b**(1-0.667)))
		cv2.normalize(VEG, VEG, 0.0, 1.0, cv2.NORM_MINMAX)
		indices[3] = np.concatenate((indices[3], VEG.ravel()))
		# cv2.normalize(VEG, VEG, 0.0, 255.0, cv2.NORM_MINMAX)
		# VEG = np.uint8(VEG)
		# cv2.imwrite("VEG.jpg", VEG)

		# ExGR
		ExGR = g-(2.4*r)-b
		cv2.normalize(ExGR, ExGR, 0.0, 1.0, cv2.NORM_MINMAX)
		indices[4] = np.concatenate((indices[4], ExGR.ravel()))
		# cv2.normalize(ExGR, ExGR, 0.0, 255.0, cv2.NORM_MINMAX)
		# ExGR = np.uint8(ExGR)
		# cv2.imwrite("ExGR.jpg", ExGR)

		# WI
		WI = Utils.div0((g-b),(abs(r-g)+1))
		cv2.normalize(WI, WI, 0.0, 1.0, cv2.NORM_MINMAX)
		indices[5] = np.concatenate((indices[5], WI.ravel()))
		# cv2.normalize(WI, WI, 0.0, 255.0, cv2.NORM_MINMAX)
		# WI = np.uint8(WI)
		# cv2.imwrite("WI.jpg", WI)

	plot_roc(gtAllImgs, indices, Utils.idxsLabels, "noFusion")
	early_fusion(gtAllImgs, indices)
	late_fusion(gtAllImgs, indices)


def main():
	# y_true = [1, 1, 1, 0]
	# y_pred = [1, 1, 0, 0]
	# print(metrics.balanced_accuracy_score(y_true,y_pred))
	global filterType
	with open(args.inputList, 'r') as file:
		lines = file.readlines()
		imgs = []
		for line in lines:
			imgs.append(line.rstrip().split(' '))
	filterType = int(args.filterType)
	process(imgs)
if __name__=='__main__':
	main()


