# Copyright 2021 Alibaba Group Holding Limited. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =============================================================================

r'''Functions for data access.
'''

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow.python.data.ops import dataset_ops
from tensorflow.python.framework import ops

from hybridbackend.tensorflow.training.detect_end import raises_out_of_range


def make_one_shot_iterator(ds, drop_remainder=None):
  r'''Wrapper of make_one_shot_iterator.

  Args:
    ds: a `tf.data.Dataset`
  '''
  with ops.device('/cpu:0'):
    with raises_out_of_range(ds, drop_remainder) as ods:
      if hasattr(dataset_ops, 'make_one_shot_iterator'):
        return dataset_ops.make_one_shot_iterator(ods)
      return ods.make_one_shot_iterator()


def make_initializable_iterator(ds, drop_remainder=None):
  r'''Wrapper of make_initializable_iterator.

  Args:
    ds: a `tf.data.Dataset`
  '''
  with ops.device('/cpu:0'):
    with raises_out_of_range(ds, drop_remainder) as ods:
      if hasattr(dataset_ops, 'make_initializable_iterator'):
        return dataset_ops.make_initializable_iterator(ods)
      return ods.make_initializable_iterator()