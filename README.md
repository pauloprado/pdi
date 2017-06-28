# pdi

No filter results
-------------
|Method|AUC|EER|FAR|FRR|Accuracy
|:----------:|:-------------:|:------:|:------:|:------:|:------:|
|NGRDI | 0.824 | 0.286	| 0.267| 0.267 | 0.733 |
|ExG | 0.805 | 0.220	| 0.280	| 0.280 | 0.720 |
|CIVE | 0.808 | 0.218	| 0.277	| 0.277 | 0.723 |
|VEG | 0.814 | 0.187| 0.269	| 0.269 | 0.731 |
|ExGR | 0.816| 0.227	| 0.273	| 0.273 | 0.727 |
|WI | 0.749| 0.284| 0.312 | 0.312 | 0.688 |
|Arithmetic Mean | 0.810 | 0.236	| 0.276	| 0.276| 0.723 |
|Geometric mean | 0.812 | 0.0008| 0.275	| 0.275 | 0.725 |

Late fusion
-------------
|Method|Accuracy
|:----------:|:-------------:|
|Majority | 0.719|


Blur results
-------------
|Method|AUC|EER|FAR|FRR|Accuracy
|:----------:|:-------------:|:------:|:------:|:------:|:------:|
|NGRDI | 0.890| 0.389	| 0.199	| 0.199 |  0.800 |
|ExG | 0.852 | 0.313	| 0.243	| 0.243 | 0.756 |
|CIVE | 0.854 | 0.313	| 0.242	| 0.242 | 0.758 |
|VEG | 0.851| 0.287	| 0.2465	| 0.246 | 0.754 |
|ExGR | 0.878 | 0.328	| 0.214	| 0.214 | 0.786 |
|WI | 0.804 | 0.348	| 0.274	| 0.274 | 0.726 |
|Arithmetic Mean | 0.862 | 0.330	| 0.233	| 0.233 | 0.767 |
|Geometric mean | 0.862 | 0.014	| 0.233	| 0.233 | 0.767 |

Late fusion
-------------
|Method|Accuracy
|:----------:|:-------------:|
|Majority | 0.759|


Gaussian filter results
-------------
|Method|AUC|EER|FAR|FRR|Accuracy
|:----------:|:-------------:|:------:|:------:|:------:|:------:|
|NGRDI | 0.867 | 0.352	| 0.223	| 0.223 | | 0.777 |
|ExG | 0.834 | 0.281	| 0.257	| 0.257 | | 0.743 |
|CIVE | 0.836 | 0.280	| 0.256	| 0.256 | | 0.744 |
|VEG | 0.834 | 0.255	| 0.257	| 0.257 | | 0.743 |
|ExGR | 0.852 | 0.291	| 0.239	| 0.239 | | 0.761 |
|WI | 0.786 | 0.328	| 0.285	| 0.285 | | 0.715 |
|Arithmetic Mean | 0.843 | 0.298	| 0.249	| 0.249 | | 0.750 |
|Geometric mean | 0.843 | 0.006	| 0.250	| 0.250 | | 0.750 |

Late fusion
-------------
|Method|Accuracy
|:----------:|:-------------:|
|Majority | 0.744|

Mean filter results
-------------
|Method|AUC|EER|FAR|FRR|Accuracy
|:----------:|:-------------:|:------:|:------:|:------:|:------:|
|NGRDI | 0.876 | 0.390	| 0.216	| 0.216 | 0.784 |
|ExG | 0.830 | 0.301	| 0.270	| 0.270 | 0.730 |
|CIVE | 0.832 | 0.300	| 0.268	| 0.268 | 0.732 |
|VEG | 0.818 | 0.265	| 0.283	| 0.283 | 0.717 |
|ExGR | 0.852 | 0.324	| 0.246	| 0.246 | 0.754 |
|WI | 0.781 | 0.340	| 0.296	| 0.296 | 0.703 |
|Arithmetic Mean | 0.840 | 0.319	| 0.260	| 0.260 | 0.740 |
|Geometric mean | 0.840 | 0.010	| 0.261	| 0.261 | 0.739 |

Late fusion
-------------
|Method|Accuracy
|:----------:|:-------------:|
|Majority | 0.729|

Bilateral filter results
-------------
|Method|AUC|EER|FAR|FRR|Accuracy
|:----------:|:-------------:|:------:|:------:|:------:|:------:|
|NGRDI | 0.828 | 0.290	| 0.264	| 0.264 | 0.736 |
|ExG | 0.808 | 0.227	| 0.278	| 0.278 | 0.722 |
|CIVE | 0.811 | 0.225	| 0.276	| 0.276 | 0.724 |
|VEG | 0.808 | 0.197	| 0.278	| 0.278 | 0.722 |
|ExGR | 0.817 | 0.231	| 0.274	| 0.274 | 0.726 |
|WI | 0.753 | 0.290	| 0.310	| 0.310 | 0.690 |
|Arithmetic Mean | 0.812 | 0.242	| 0.277	| 0.277 | 0.723 |
|Geometric mean | 0.813 | 0.001	| 0.276	| 0.276 | 0.724 |

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

No filter results
-------------
|Method|AUC|EER|FAR|FRR|Accuracy
|:----------:|:-------------:|:------:|:------:|:------:|:------:|
|NGRDI|0.790|0.428|0.290|0.290|0.710|
|ExG|0.801|0.311|0.268|0.268|0.732|
|CIVE|0.800|0.311|0.268|0.268|0.732|
|VEG|0.783|0.274|0.289|0.289|0.711|
|ExGR|0.777|0.374|0.302|0.302|0.698|
|WI|0.788|0.320|0.277|0.277|0.723|
|Arithmetic Mean|0.802|0.337|0.267|0.267|0.733|
|Geometric mean|0.802|0.015|0.268|0.268|0.732|

Late fusion
-------------
|Method|Accuracy
|:----------:|:-------------:|
|Majority|0.735|

Blur results
-------------
|Method|AUC|EER|FAR|FRR|Accuracy
|:----------:|:-------------:|:------:|:------:|:------:|:------:|
|NGRDI|0.865|0.509|0.209|0.209|0.791|
|ExG|0.861|0.388|0.215|0.215|0.785|
|CIVE|0.863|0.390|0.214|0.214|0.786|
|VEG|0.853|0.367|0.225|0.225|0.775|
|ExGR|0.860|0.462|0.212|0.212|0.788|
|WI|0.808|0.383|0.258|0.258|0.742|
|Arithmetic Mean|0.871|0.418|0.206|0.206|0.794|
|Geometric mean|0.871|0.115|0.206|0.206|0.794|

Late fusion
-------------
|Method|Accuracy
|:----------:|:-------------:|
|Majority|0.785|


Gaussian filter results
-------------
|Method|AUC|EER|FAR|FRR|Accuracy
|:----------:|:-------------:|:------:|:------:|:------:|:------:|
|NGRDI|0.849|0.480|0.232|0.232|0.768|
|ExG|0.849|0.361|0.230|0.230|0.770|
|CIVE|0.851|0.363|0.228|0.228|0.772|
|VEG|0.840|0.338|0.238|0.238|0.762|
|ExGR|0.840|0.432|0.240|0.240|0.760|
|WI|0.809|0.361|0.257|0.257|0.743|
|Arithmetic Mean|0.858|0.389|0.223|0.223|0.777|
|Geometric mean|0.858|0.060|0.224|0.224|0.776|

Late fusion
-------------
|Method|Accuracy
|:----------:|:-------------:|
|Majority|0.770|


Mean filter results
-------------
|Method|AUC|EER|FAR|FRR|Accuracy
|:----------:|:-------------:|:------:|:------:|:------:|:------:|
|NGRDI|0.859|0.502|0.215|0.215|0.785|
|ExG|0.852|0.391|0.224|0.224|0.776|
|CIVE|0.853|0.392|0.223|0.223|0.777|
|VEG|0.838|0.362|0.238|0.238|0.762|
|ExGR|0.845|0.454|0.226|0.226|0.774|
|WI|0.812|0.385|0.254|0.254|0.746|
|Arithmetic Mean|0.861|0.415|0.215|0.215|0.785|
|Geometric mean|0.861|0.108|0.216|0.216|0.784|

Late fusion
-------------
|Method|Accuracy
|:----------:|:-------------:|
|Majority|0.777|


Bilateral filter results
-------------
|Method|AUC|EER|FAR|FRR|Accuracy
|:----------:|:-------------:|:------:|:------:|:------:|:------:|
|NGRDI|0.806|0.437|0.280|0.280|0.720|
|ExG|0.813|0.322|0.262|0.262|0.738|
|CIVE|0.813|0.323|0.262|0.262|0.738|
|VEG|0.796|0.288|0.282|0.282|0.718|
|ExGR|0.793|0.380|0.293|0.293|0.707|
|WI|0.792|0.329|0.277|0.277|0.723|
|Arithmetic Mean|0.815|0.348|0.260|0.260|0.740|
|Geometric mean|0.816|0.021|0.261|0.261|0.739|

Late fusion
-------------
|Method|Accuracy
|:----------:|:-------------:|
|Majority|0.740|


Raw indices: 
![alt text][raw2]

Early fusion:
![alt text][early2]

[raw2]: results/Figure_1_lcrs2.png
[early2]: results/Figure_early_fusion_lcrs2.png