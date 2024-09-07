import tempfile


def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.

    :param results: unicode string
    :return: path of the temporary file
    '''

=======
#!/usr/bin/env python
# encoding: utf-8
"""
test_util.py

Created by <NAME> on 2009-11-05.
Copyright (c) 2009-2015 Exa Networks. All rights reserved.
"""

import unittest

from exabgp.util import ordinal
from exabgp.util import character
from exabgp.util import concat_bytes_i
from exabgp.util import concat_bytes_b

from exabgp.util import split_bytes
from exabgp.util import hexstring
from exabgp.util import hexs
from exabgp.util import hex
from exabgp.util import character
from exabgp.util import ordinal

from exabgp.util import concat_bytes
from exabgp.util import split