'''


import os
import sys
import time
import logging
import argparse
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.optim.lr_scheduler import StepLR
from torch.utils.data import DataLoader
from tensorboardX import SummaryWriter
from tqdm import tqdm

from dataset import Dataset
from model import Model

parser = argparse.ArgumentParser(description='PyTorch implementation of Deep-Hash')
parser.add_argument('--data_dir', type=str, default='data/train', help='path to dataset')
parser.add_argument('--batch_size', type=int, default=128, help='batch size')
parser.add_argument('--num_workers', type=int, default=4, help='number of workers')
parser.add_argument('--epochs', type=int, default=200, help='number of training epochs')
parser.add_argument('--lr', type=float, default=0.001, help='learning rate')
parser.add_argument('--lr_decay_step', type=