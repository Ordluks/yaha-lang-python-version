import unittest
from compiller.parser import parser
from compiller.data import *


class TestParser(unittest.TestCase):
  def test_error(self):
    tokens = [
      Token(INTEGER, '10')
    ]
    
    with self.assertRaises(SystemExit):
      parser(tokens)
    
  def test_func(self):
    tokens = [
      Token(FUNC_KW, 'func'),
      Token(NAME, 'main'),
      
    ]
    
    ast = parser(tokens)
    print(vars(ast))
    self.assertTrue(True)
