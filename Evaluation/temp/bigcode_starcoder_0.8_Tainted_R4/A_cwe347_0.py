'''

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

import sys
import os
import pandas as pd
import dask.dataframe as dd

from. import io as mlio

import warnings

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    import tensorflow as tf
    import tensorflow.keras as keras
    import tensorflow.keras.layers as keras_layers
    import tensorflow.keras.models as keras_models
    import sklearn

from. import core

tf.config.set_visible_devices([], "GPU")

