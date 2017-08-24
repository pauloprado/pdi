import numpy as np

# Vegetation indices
idxsLabels = ['NGRDI', 'ExG', 'CIVE', 'VEG', 'ExGR', 'WI']

# Early fusion methods
earlyFusonLabels = ['Arithmetic Mean', 'Geometric mean']

# Late fusion method
lateFusionLabels = ['Majority']


filters = ['No Filter', 'Blur', 'Gaussian Filter', 'Mean Filter', 'Bilateral Filter']

'''
	Function that doesnt let the division per zero five a NaN, substitute for 0 instead
	@param a The dividend
	@param b The divisor
'''
def div0( a, b ):
    with np.errstate(divide='ignore', invalid='ignore'):
        c = np.true_divide( a, b )
        c[ ~ np.isfinite( c )] = 0
    return c

def buildFileName(filterType, fusion, outputDir):
	return outputDir+"/"+fusion+"_"+filters[filterType].replace(' ','')+".png"
