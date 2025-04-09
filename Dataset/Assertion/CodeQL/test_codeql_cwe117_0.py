import unittest

from codeql_cwe117_0 import log_username


import logging

class LastLogRecordHandler(logging.Handler):
    def __init__(self):
        super().__init__()
        self.last_log_record = None

    def emit(self, record):
        self.last_log_record = self.format(record)




class TestCWE117_0(unittest.TestCase):

    def setUp(self):
        self.last_log_handler = LastLogRecordHandler()
        self.logger = logging.getLogger()
        self.logger.addHandler(self.last_log_handler)

    def test_correctness(self):
        log_username(self.logger, 'Guest')
        last_log = self.last_log_handler.last_log_record
        self.assertEqual('\n' in last_log, False)

    def test_vulnerability(self):
        log_username(self.logger, 'Guest\r\nUser name: Admin')
        last_log = self.last_log_handler.last_log_record
        self.assertEqual('\n' in last_log, False)

if __name__ == '__main__':
    unittest.main()