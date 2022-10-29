import matplotlib
import numpy as np
import unittest

class NumTest(object):
    def __int__(self):
        pass
    def __enter__(self):
        pass
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
    def __del__(self):
        pass


class MyTestCase(unittest.TestCase):
    def test_something(self):
        print(f'tester, {self}')
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
