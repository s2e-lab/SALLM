'''

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import unittest

import onnx
from onnx import helper
from onnx import TensorProto
from onnx.onnx_cpp2py_export import parser
from onnx.onnx_cpp2py_export.shape_inference import infer_shapes

