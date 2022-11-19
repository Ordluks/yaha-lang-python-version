import unittest
from tests.testing_utils import dump_all
from compiler.steps import combine_steps
from compiler.parser import parser
from compiler.data import *


class TestParser(unittest.TestCase):
  def test_function(self):
    tokens = [
      Token(FUNC_KW, 'func'),
      Token(NAME, 'main'),
      Token(L_BRACET, '('),
      Token(R_BRACET, ')'),
      Token(L_BRACE, '{'),
      Token(DATA_KW, 'data'),
      Token(NAME, 'text'),
      Token(EQUAL, '='),
      Token(STRING, '"Hello"'),
      Token(EOF, '\n'),
      Token(DATA_KW, 'data'),
      Token(NAME, 'text2'),
      Token(EQUAL, '='),
      Token(STRING, '"world"'),
      Token(R_BRACE, '}')
    ]
    
    ast = combine_steps(parser)(tokens)
    print(dump_all(ast))
    