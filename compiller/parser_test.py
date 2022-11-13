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
      Token(L_BRACE, '{'),
      Token(DATA_KW, 'data'),
      Token(NAME, 'msg'),
      Token(EQUAL, '='),
      Token(STRING, '"hello"'),
      Token(R_BRACE, '}')
    ]
    
    ast = parser(tokens)
    print(vars(ast))
    print(list(map(vars, ast.functions)))
    self.assertTrue(True)
