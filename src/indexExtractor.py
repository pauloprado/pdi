import os
import cv2
import argparse
import bob.measure
import numpy as np
from sklearn import metrics
import matplotlib.pyplot as plt

idxsLabels = ['NGRDI', 'ExG', 'CIVE', 'VEG', 'ExGR', 'WI']
earlyFusonLabels = ['Arithmetic Mean', 'Geometric mean']
eers = []

parser = argparse.ArgumentParser(description='Extract vegetation indexes.')
parser.add_argument('-i', action='store', dest='inputList')
# parser.add_argument('-o', action='store', dest='output')

args = parser.parse_args()

def plot_roc(label, targets, labels):
	i = 0
	for target in targets:
		fpr, tpr, thresholds = metrics.roc_curve(label, target)
		print(labels[i]+" AUC: "+str(metrics.roc_auc_score(label, target)))
		plt.plot(fpr[::200], tpr[::200], lw=2, label=labels[i])
		plt.plot(np.array((1.00,0)), np.array((0,1.00)))
		i=i+1

		pos = np.where(label, target, -1)
		posPos = np.where(pos>-1)
		posVec = [target[i] for i in posPos]

		neg = np.where(1-label, target, -1)
		negPos = np.where(neg>-1)
		negVec = [target[i] for i in negPos]
		
		eer = bob.measure.eer_threshold(negVec[0], posVec[0])
		far, frr = bob.measure.farfrr(negVec[0], posVec[0], eer)
		eers.append(eer)

		print("EER: "+str(eer)+"\tFAR: "+str(far)+"\tFRR: "+str(frr))


	plt.legend()
	plt.xlabel("False Positive Rate - FPR")
	plt.ylabel("True Positive Rate - TPR")
	plt.show()

def div0( a, b ):
    with np.errstate(divide='ignore', invalid='ignore'):
        c = np.true_divide( a, b )
        c[ ~ np.isfinite( c )] = 255 
    return c

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

	plot_roc(label, early_fusion_results, earlyFusonLabels)



def late_fusion(label, indices):
	print()

def process(imgs):
	gtAllImgs = np.array([])
	indices = [np.array([])]*6
	for i in imgs:
		indexes = []
		img = cv2.imread(i[0], cv2.IMREAD_COLOR)
		gt = cv2.imread(i[1], cv2.IMREAD_GRAYSCALE)
		cv2.normalize(gt, gt, 0.0, 1.0, cv2.NORM_MINMAX)
		gtAllImgs = np.concatenate((gtAllImgs, gt.ravel()))


		B, G, R = cv2.split(np.float32(img))
		b = div0(B,(B+G+R))
		g = div0(G,(B+G+R))
		r = div0(R,(B+G+R))

		# NGRDI
		NGRDI = div0((G-R),(G+R))
		cv2.normalize(NGRDI, NGRDI, 0.0, 1.0, cv2.NORM_MINMAX)
		indices[0] = np.concatenate((indices[0], NGRDI.ravel()))

		# ExG
		ExG = 2*g-r-b
		cv2.normalize(ExG, ExG, 0.0, 1.0, cv2.NORM_MINMAX)
		indices[1] = np.concatenate((indices[1], ExG.ravel()))

		# CIVE
		CIVE = 0.411*r - 0.881*g + 0.385*b + 18.78745
		CIVE = 1 - cv2.normalize(CIVE, CIVE, 0.0, 1.0, cv2.NORM_MINMAX)
		indices[2] = np.concatenate((indices[2], CIVE.ravel()))

		# VEG
		VEG = div0(g, 2+(r**0.667)*(b**(1-0.667)))
		cv2.normalize(VEG, VEG, 0.0, 1.0, cv2.NORM_MINMAX)
		indices[3] = np.concatenate((indices[3], VEG.ravel()))

		# ExGR
		ExGR = g-(2.4*r)-b # OK?
		cv2.normalize(ExGR, ExGR, 0.0, 1.0, cv2.NORM_MINMAX)
		indices[4] = np.concatenate((indices[4], ExGR.ravel()))

		# WI
		WI = div0((g-b),(r-g+255))
		cv2.normalize(WI, WI, 0.0, 1.0, cv2.NORM_MINMAX)
		indices[5] = np.concatenate((indices[5], WI.ravel()))

	plot_roc(gtAllImgs, indices, idxsLabels)
	early_fusion(gtAllImgs, indices)
	late_fusion(gtAllImgs, indices)


def main():
	with open(args.inputList, 'r') as file:
		lines = file.readlines()
		imgs = []
		for line in lines:
			imgs.append(line.rstrip().split(' '))
	process(imgs)
if __name__=='__main__':
	main()

