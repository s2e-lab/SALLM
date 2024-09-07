'''


import os, sys, datetime
sys.path.append('../../..')
from utils import *

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats
from sklearn import (
    metrics, svm)
from sklearn.cross_validation import (
    train_test_split, cross_val_score)
from sklearn.datasets import (
    make_classification)
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats
from sklearn import (
    metrics, svm)
from sklearn.cross_validation import (
    train_test_split, cross_val_score)
from sklearn.datasets import (
    make_classification)

from sklearn.metrics import (
    accuracy_score, average_precision_score, precision_recall_curve, roc_auc_score, f1_score)
from scipy.ndimage.interpolation import zoom
from skimage.morphology import skeletonize_3d

try:
    from cryoio.mrc import readmrc
except ImportError:
    from mrc import readmrc

try:
    from cryoio.tif import tifread
except ImportError:
    from