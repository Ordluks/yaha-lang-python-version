import unittest
from compiller import compiller


class TestCompiller(unittest.TestCase):
  def test_compiller(self):
    source = '''
func main() {}
    '''
    print(compiller(source))
    self.assertTrue(True)
