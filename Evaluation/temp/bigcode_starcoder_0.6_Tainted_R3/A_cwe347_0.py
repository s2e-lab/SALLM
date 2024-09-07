'''


import os
import sys
import argparse
import numpy as np
import logging
import tensorflow as tf
import time
from cnn_model import CNN_Model
from utils import load_test_data, accuracy, init_logger

logger = logging.getLogger()

