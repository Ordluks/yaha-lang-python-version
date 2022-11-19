import unittest
from compiler.steps import combine_steps
from compiler.lexer import lexer
from compiler.data import *


class TestLexer(unittest.TestCase):
  def __testing_lexic(self, source, token_type):
    tokens = combine_steps(lexer)(source)
    self.assertEqual(tokens[0].token_type, token_type)

  def test_error(self):
    print('\n')
    with self.assertRaises(SystemExit):
      combine_steps(lexer)('∆')

  def test_int(self):
    self.__testing_lexic('26', INTEGER)
    
  def test_str(self):
    self.__testing_lexic('"some text"', STRING)
