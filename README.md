# pdi

No filter results
-------------
|Method|AUC|EER|FAR|FRR
|:----------:|:-------------:|:------:|:------:|:------:|
|NGRDI | 0.824 | 0.286	| 0.267| 0.267 |
|ExG | 0.805 | 0.220	| 0.280	| 0.280 |
|CIVE | 0.808 | 0.218	| 0.277	| 0.277 |
|VEG | 0.814 | 0.187| 0.269	| 0.269 |
|ExGR | 0.816| 0.227	| 0.273	| 0.273 |
|WI | 0.749| 0.284| 0.312 | 0.312 |
|Arithmetic Mean | 0.810 | 0.236	| 0.276	| 0.276|
|Geometric mean | 0.812 | 0.0008| 0.275	| 0.275 |

Late fusion
-------------
|Method|Accuracy
|:----------:|:-------------:|
|Majority | 0.719|


Blur results
-------------
|Method|AUC|EER|FAR|FRR
|:----------:|:-------------:|:------:|:------:|:------:|
|NGRDI | 0.890| 0.389	| 0.199	| 0.199 |
|ExG | 0.852 | 0.313	| 0.243	| 0.243 |
|CIVE | 0.854 | 0.313	| 0.242	| 0.242 |
|VEG | 0.851| 0.287	| 0.2465	| 0.246 |
|ExGR | 0.878 | 0.328	| 0.214	| 0.214 |
|WI | 0.804 | 0.348	| 0.274	| 0.274 |
|Arithmetic Mean | 0.862 | 0.330	| 0.233	| 0.233 |
|Geometric mean | 0.862 | 0.014	| 0.233	| 0.233 |

Late fusion
-------------
|Method|Accuracy
|:----------:|:-------------:|
|Majority | 0.759|


Gaussian filter results
-------------
|Method|AUC|EER|FAR|FRR
|:----------:|:-------------:|:------:|:------:|:------:|
|NGRDI | 0.867 | 0.352	| 0.223	| 0.223 |
|ExG | 0.834 | 0.281	| 0.257	| 0.257 |
|CIVE | 0.836 | 0.280	| 0.256	| 0.256 |
|VEG | 0.834 | 0.255	| 0.257	| 0.257 |
|ExGR | 0.852 | 0.291	| 0.239	| 0.239 |
|WI | 0.786 | 0.328	| 0.285	| 0.285 |
|Arithmetic Mean | 0.843 | 0.298	| 0.249	| 0.249 |
|Geometric mean | 0.843 | 0.006	| 0.250	| 0.250 |

Late fusion
-------------
|Method|Accuracy
|:----------:|:-------------:|
|Majority | 0.744|

Mean filter results
-------------
|Method|AUC|EER|FAR|FRR
|:----------:|:-------------:|:------:|:------:|:------:|
|NGRDI | 0.876 | 0.390	| 0.216	| 0.216 |
|ExG | 0.830 | 0.301	| 0.270	| 0.270 |
|CIVE | 0.832 | 0.300	| 0.268	| 0.268 |
|VEG | 0.818 | 0.265	| 0.283	| 0.283 |
|ExGR | 0.852 | 0.324	| 0.246	| 0.246 |
|WI | 0.781 | 0.340	| 0.296	| 0.296 |
|Arithmetic Mean | 0.840 | 0.319	| 0.260	| 0.260 |
|Geometric mean | 0.840 | 0.010	| 0.261	| 0.261 |

Late fusion
-------------
|Method|Accuracy
|:----------:|:-------------:|
|Majority | 0.729|

Bilateral filter results
-------------
|Method|AUC|EER|FAR|FRR
|:----------:|:-------------:|:------:|:------:|:------:|
|NGRDI | 0.828 | 0.290	| 0.264	| 0.264 |
|ExG | 0.808 | 0.227	| 0.278	| 0.278 |
|CIVE | 0.811 | 0.225	| 0.276	| 0.276 |
|VEG | 0.808 | 0.197	| 0.278	| 0.278 |
|ExGR | 0.817 | 0.231	| 0.274	| 0.274 |
|WI | 0.753 | 0.290	| 0.310	| 0.310 |
|Arithmetic Mean | 0.812 | 0.242	| 0.277	| 0.277 |
|Geometric mean | 0.813 | 0.001	| 0.276	| 0.276 |

Late fusion
-------------
|Method|Accuracy
|:----------:|:-------------:|
|Majority | 0.720|


------------------

No filter: 
![alt text][nofilter]

Early fusion:
![alt text][nofilter_early_fusion]

[nofilter]: results/nofilter.png
[nofilter_early_fusion]: results/nofilter_early_fusion.png

Blur: 
![alt text][blur]

Early fusion:
![alt text][blur_early]

[blur]: results/blur.png
[blur_early]: results/blur_early.png

Gaussian filter: 
![alt text][gaussian_blur]

Early fusion:
![alt text][gaussian_blur_early]

[gaussian_blur]: results/gaussian_blur.png
[gaussian_blur_early]: results/gaussian_blur_early.png

Mean filter: 
![alt text][mean]

Early fusion:
![alt text][mean_early]

[mean]: results/mean.png
[mean_early]: results/mean_early.png

Bilateral filter: 
![alt text][bilateral]

Early fusion:
![alt text][bilateral_early]

[bilateral]: results/bilateral.png
[bilateral_early]: results/bilateral_early.png

-----------------
Database LCRS2
-------------------
-------------
|Method|AUC|EER|FAR|FRR
|:----------:|:-------------:|:------:|:------:|:------:|
| NGRDI|  0.790 | 0.428 | 0.290 | 0.290 |
| ExG |    0.805   |   0.311 | 0.268 | 0.268 |
| CIVE | 0.800 | 0.311 | 0.268 | 0.268 |
| VEG | 0.783 | 0.273 | 0.288 | 0.288 |
|ExGR | 0.777 | 0.374 | 0.302 | 0.302 |
| WI | 0.788 | 0.320 | 0.277 | 0.277 |
| Arithmetic Mean | 0.802 | 0.337 | 0.266 | 0.266 |
| Geometric Mean | 0.802 | 0.015| 0.268 | 0.268 |

------------------

Raw indices: 
![alt text][raw2]

Early fusion:
![alt text][early2]

[raw2]: results/Figure_1_lcrs2.png
[early2]: results/Figure_early_fusion_lcrs2.png