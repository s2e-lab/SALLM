'''


import os
import sys
import json
import time
import shutil
import numpy as np
import pandas as pd
import argparse
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.utils import class_weight
import matplotlib.pyplot as plt

# Import custom modules
from config import config
from data_generator import DataGenerator
from data_generator import DataGeneratorTest
from utils import get_data
from utils import plot_confusion_matrix

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument('--model_name', type=str, default='resnet18', help='Name of the model.')
parser.add_argument('--dataset', type=str, default='chest_xray', help='Dataset to use.')
parser.add_argument('--img_size', type=int, default=224, help='Image size.')
parser.add_argument('--batch_size', type