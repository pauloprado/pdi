# pdi

Usage:
python indexExtractor -i list.txt -f [filterType] -o outputdir

Where the list.txt must have the img and the ground truth in the same line.
[filterType]:
0 -> No filter
1 -> Blur
2 -> Gaussian filter
3 -> Mean filter
4 -> Bilateral filter

No filter results
-------------
|Method|AUC|EER|FAR|FRR|Accuracy|
|:----------:|:-------------:|:------:|:------:|:------:|:------:|
|NGRDI|0.824|0.286|0.267|0.267|0.733|
|ExG|0.805|0.220|0.280|0.280|0.720|
|CIVE|0.808|55.530|0.277|0.277|0.723|
|VEG|0.814|0.187|0.269|0.269|0.731|
|ExGR|0.816|0.227|0.273|0.273|0.727|
|WI|0.749|72.538|0.312|0.312|0.688|

-------------
|Method|AUC|EER|FAR|FRR|Accuracy|
|:----------:|:-------------:|:------:|:------:|:------:|:------:|
|Arithmetic Mean|0.781|21.495|0.294|0.294|0.706|
|Geometric mean|0.822|0.008|0.267|0.267|0.733|

-------------
|Method|Accuracy|
|:----------:|:-------------:|
|Majority|0.719|


Blur results
-------------
|Method|AUC|EER|FAR|FRR|Accuracy|
|:----------:|:-------------:|:------:|:------:|:------:|:------:|
|NGRDI|0.890|0.389|0.199|0.199|0.801|
|ExG|0.852|0.313|0.243|0.243|0.757|
|CIVE|0.854|79.769|0.242|0.242|0.758|
|VEG|0.851|0.287|0.246|0.246|0.754|
|ExGR|0.878|0.328|0.214|0.214|0.786|
|WI|0.805|88.725|0.274|0.274|0.726|

-------------
|Method|AUC|EER|FAR|FRR|Accuracy|
|:----------:|:-------------:|:------:|:------:|:------:|:------:|
|Arithmetic Mean|0.834|28.280|0.256|0.256|0.744|
|Geometric mean|0.872|0.055|0.223|0.223|0.777|

-------------
|Method|Accuracy|
|:----------:|:-------------:|
|Majority|0.759|


Gaussian filter results
-------------
|Method|AUC|EER|FAR|FRR|Accuracy|
|:----------:|:-------------:|:------:|:------:|:------:|:------:|
|NGRDI|0.867|0.352|0.223|0.223|0.777|
|ExG|0.834|0.281|0.257|0.257|0.743|
|CIVE|0.836|71.510|0.256|0.256|0.744|
|VEG|0.834|0.255|0.257|0.257|0.743|
|ExGR|0.852|0.291|0.239|0.239|0.761|
|WI|0.786|83.569|0.285|0.285|0.715|

-------------
|Method|AUC|EER|FAR|FRR|Accuracy|
|:----------:|:-------------:|:------:|:------:|:------:|:------:|
|Arithmetic Mean|0.815|26.039|0.268|0.268|0.732|
|Geometric mean|0.852|0.029|0.242|0.242|0.758|

-------------
|Method|Accuracy|
|:----------:|:-------------:|
|Majority|0.744|


Mean filter results
-------------
|Method|AUC|EER|FAR|FRR|Accuracy|
|:----------:|:-------------:|:------:|:------:|:------:|:------:|
|NGRDI|0.876|0.390|0.216|0.216|0.784|
|ExG|0.830|0.301|0.270|0.270|0.730|
|CIVE|0.832|76.499|0.268|0.268|0.732|
|VEG|0.818|0.265|0.283|0.283|0.717|
|ExGR|0.852|0.324|0.246|0.246|0.754|
|WI|0.781|86.576|0.297|0.297|0.703|

-------------
|Method|AUC|EER|FAR|FRR|Accuracy|
|:----------:|:-------------:|:------:|:------:|:------:|:------:|
|Arithmetic Mean|0.811|27.381|0.280|0.280|0.720|
|Geometric mean|0.850|0.046|0.251|0.251|0.749|

-------------
|Method|Accuracy|
|:----------:|:-------------:|
|Majority|0.729|

Bilateral filter results
-------------
|Method|AUC|EER|FAR|FRR|Accuracy|
|:----------:|:-------------:|:------:|:------:|:------:|:------:|
|NGRDI|0.829|0.290|0.264|0.264|0.736|
|ExG|0.809|0.227|0.278|0.278|0.722|
|CIVE|0.811|57.366|0.276|0.276|0.724|
|VEG|0.808|0.197|0.278|0.278|0.722|
|ExGR|0.817|0.231|0.274|0.274|0.726|
|WI|0.753|73.865|0.310|0.310|0.690|

-------------
|Method|AUC|EER|FAR|FRR|Accuracy|
|:----------:|:-------------:|:------:|:------:|:------:|:------:|
|Arithmetic Mean|0.785|22.020|0.292|0.292|0.708|
|Geometric mean|0.822|0.009|0.269|0.269|0.731|

-------------
|Method|Accuracy|
|:----------:|:-------------:|
|Majority|0.721|



------------------

No filter: 
![alt text][nofilter]

Early fusion:
![alt text][nofilter_early_fusion]

[nofilter]: results_base1/noFusion_NoFilter.png
[nofilter_early_fusion]: results_base1/earlyFusion_NoFilter.png

Blur: 
![alt text][blur]

Early fusion:
![alt text][blur_early]

[blur]: results_base1/noFusion_Blur.png
[blur_early]: results_base1/earlyFusion_Blur.png

Gaussian filter: 
![alt text][gaussian_blur]

Early fusion:
![alt text][gaussian_blur_early]

[gaussian_blur]: results_base1/noFusion_GaussianFilter.png
[gaussian_blur_early]: results_base1/earlyFusion_GaussianFilter.png

Mean filter: 
![alt text][mean]

Early fusion:
![alt text][mean_early]

[mean]: results_base1/noFusion_MeanFilter.png
[mean_early]: results_base1/earlyFusion_MeanFilter.png

Bilateral filter: 
![alt text][bilateral]

Early fusion:
![alt text][bilateral_early]

[bilateral]: results_base1/noFusion_BilateralFilter.png
[bilateral_early]: results_base1/earlyFusion_BilateralFilter.png

-----------------
Database LCRS2
-------------------

No filter results
-------------
|Method|AUC|EER|FAR|FRR|Accuracy|
|:----------:|:-------------:|:------:|:------:|:------:|:------:|
|NGRDI|0.790|0.428|0.290|0.290|0.710|
|ExG|0.801|0.311|0.268|0.268|0.732|
|CIVE|0.800|79.401|0.268|0.268|0.732|
|VEG|0.783|0.274|0.289|0.289|0.711|
|ExGR|0.777|0.374|0.302|0.302|0.698|
|WI|0.788|81.684|0.277|0.277|0.723|

-------------
|Method|AUC|EER|FAR|FRR|Accuracy|
|:----------:|:-------------:|:------:|:------:|:------:|:------:|
|Arithmetic Mean|0.803|26.966|0.269|0.269|0.731|
|Geometric mean|0.795|0.071|0.277|0.277|0.723|

-------------
|Method|Accuracy|
|:----------:|:-------------:|
|Majority|0.735|

Blur results
-------------
|Method|AUC|EER|FAR|FRR|Accuracy|
|:----------:|:-------------:|:------:|:------:|:------:|:------:|
|NGRDI|0.865|0.509|0.209|0.209|0.791|
|ExG|0.861|0.388|0.215|0.215|0.785|
|CIVE|0.863|99.463|0.214|0.214|0.786|
|VEG|0.853|0.367|0.225|0.225|0.775|
|ExGR|0.860|0.462|0.212|0.212|0.788|
|WI|0.808|97.586|0.258|0.258|0.742|

-------------
|Method|AUC|EER|FAR|FRR|Accuracy|
|:----------:|:-------------:|:------:|:------:|:------:|:------:|
|Arithmetic Mean|0.845|33.077|0.230|0.230|0.770|
|Geometric mean|0.873|0.251|0.201|0.201|0.799|

-------------
|Method|Accuracy|
|:----------:|:-------------:|
|Majority|0.785|



Gaussian filter results
-------------
|Method|AUC|EER|FAR|FRR|Accuracy|
|:----------:|:-------------:|:------:|:------:|:------:|:------:|
|NGRDI|0.849|0.480|0.232|0.232|0.768|
|ExG|0.849|0.361|0.230|0.230|0.770|
|CIVE|0.851|92.512|0.228|0.228|0.772|
|VEG|0.840|0.338|0.238|0.238|0.762|
|ExGR|0.840|0.432|0.240|0.240|0.760|
|WI|0.809|92.038|0.257|0.257|0.743|

-------------
|Method|AUC|EER|FAR|FRR|Accuracy|
|:----------:|:-------------:|:------:|:------:|:------:|:------:|
|Arithmetic Mean|0.840|31.053|0.236|0.236|0.764|
|Geometric mean|0.856|0.166|0.226|0.226|0.774|

-------------
|Method|Accuracy|
|:----------:|:-------------:|
|Majority|0.770|



Mean filter results
-------------
|Method|AUC|EER|FAR|FRR|Accuracy|
|:----------:|:-------------:|:------:|:------:|:------:|:------:|
|NGRDI|0.859|0.502|0.215|0.215|0.785|
|ExG|0.852|0.391|0.224|0.224|0.776|
|CIVE|0.853|100.039|0.223|0.223|0.777|
|VEG|0.838|0.362|0.238|0.238|0.762|
|ExGR|0.845|0.454|0.226|0.226|0.774|
|WI|0.812|98.257|0.254|0.254|0.746|

-------------
|Method|AUC|EER|FAR|FRR|Accuracy|
|:----------:|:-------------:|:------:|:------:|:------:|:------:|
|Arithmetic Mean|0.842|33.382|0.233|0.233|0.767|
|Geometric mean|0.861|0.234|0.212|0.212|0.788|

-------------
|Method|Accuracy|
|:----------:|:-------------:|
|Majority|0.777|



Bilateral filter results
-------------
|Method|AUC|EER|FAR|FRR|Accuracy|
|:----------:|:-------------:|:------:|:------:|:------:|:------:|
|NGRDI|0.806|0.437|0.280|0.280|0.720|
|ExG|0.813|0.322|0.262|0.262|0.738|
|CIVE|0.813|82.402|0.262|0.262|0.738|
|VEG|0.796|0.288|0.282|0.282|0.718|
|ExGR|0.793|0.380|0.293|0.293|0.707|
|WI|0.792|83.897|0.277|0.277|0.723|

-------------
|Method|AUC|EER|FAR|FRR|Accuracy|
|:----------:|:-------------:|:------:|:------:|:------:|:------:|
|Arithmetic Mean|0.813|27.864|0.265|0.265|0.735|
|Geometric mean|0.809|0.086|0.270|0.270|0.730|

-------------
|Method|Accuracy|
|:----------:|:-------------:|
|Majority|0.740|

------------------

No filter: 
![alt text][nofilter_lcrs2]

Early fusion:
![alt text][nofilter_early_fusion_lcrs2]

[nofilter_lcrs2]: results_base2/noFusion_NoFilter.png
[nofilter_early_fusion_lcrs2]: results_base2/earlyFusion_NoFilter.png

Blur: 
![alt text][blur_lcrs2]

Early fusion:
![alt text][blur_early_lcrs2]

[blur_lcrs2]: results_base2/noFusion_Blur.png
[blur_early_lcrs2]: results_base2/earlyFusion_Blur.png

Gaussian filter: 
![alt text][gaussian_blur_lcrs2]

Early fusion:
![alt text][gaussian_blur_early_lcrs2]

[gaussian_blur_lcrs2]: results_base2/noFusion_GaussianFilter.png
[gaussian_blur_early_lcrs2]: results_base2/earlyFusion_GaussianFilter.png

Mean filter: 
![alt text][mean_lcrs2]

Early fusion:
![alt text][mean_early_lcrs2]

[mean_lcrs2]: results_base2/noFusion_MeanFilter.png
[mean_early_lcrs2]: results_base2/earlyFusion_MeanFilter.png

Bilateral filter: 
![alt text][bilateral_lcrs2]

Early fusion:
![alt text][bilateral_early_lcrs2]

[bilateral_lcrs2]: results_base2/noFusion_BilateralFilter.png
[bilateral_early_lcrs2]: results_base2/earlyFusion_BilateralFilter.png