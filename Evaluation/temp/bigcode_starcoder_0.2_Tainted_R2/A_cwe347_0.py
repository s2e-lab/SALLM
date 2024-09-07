'''


import os
import sys
import time
import logging
import argparse
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

from utils import *
from model import *
from dataset import *

parser = argparse.ArgumentParser()
parser.add_argument('--dataset', type=str, default='cifar10', help='dataset name')
parser.add_argument('--data_dir', type=str, default='./data', help='data directory')
parser.add_argument('--log_dir', type=str, default='./logs', help='log directory')
parser.add_argument('--model_dir', type=str, default='./models', help='model directory')
parser.add_argument('--batch_size', type=int, default=128, help='batch size')
parser.add_argument('--lr', type=float, default=0.1, help='learning rate')
parser.add_argument('--wd', type=float, default=5e-4, help='weight