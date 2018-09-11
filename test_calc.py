"""
Sum of two numbers test class.
"""
import unittest

from calc import sum

class TestSum(unittest.TestCase):
  """
  Sum of two numbers test class.
  """

  def setUp(self):
    """ Initialise test suite - no-op. """
    pass

  def tearDown(self):
    """ Clean up test suite - no-op. """
    pass

  def test_sum(self):
    """ Test sum(1, 1). """
    self.assertEqual(2, sum(1, 1))

if __name__ == '__main__':
  unittest.main()
