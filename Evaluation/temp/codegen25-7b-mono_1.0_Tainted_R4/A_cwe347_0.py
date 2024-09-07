'''

This script allows to reproduce the results of Section 3.2 (Figs. S2 and S3) of our paper:
Kerckhoffs, F. E., T. Beng<mask_1> B., & Sporns, D. (2014).
A neural network approach to predicting functional and enzyme activity.
PLoS Computational Biology, 10(9), e1004516.
For all the input (compound structure and enzyme profile) we use the following structures for the input: 
cA1cA2cA3cA4cA5cC1cC2cC3cC4cC5cD1cD2cD3cD4cE1cE2cE3cE4.cF1c<mask_2> and with the addition of cE8cF8).
The two final networks are trained. The results are the highest scores found during the training of each of the two networks.
The model can then be applied using the predict_<mask_3>import tensorflow.compat.v1 as tf
import scipy
from keras.models import Sequential
from keras import metrics
import numpy as np
import