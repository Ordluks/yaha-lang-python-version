import unittest
from compiler.steps import combine_steps


class TestCombineSteps(unittest.TestCase):
  def test_combine_steps(self):
    def some_step(data, raise_error):
      pass
    result = combine_steps(some_step)
    self.assertTrue(callable(result))
  