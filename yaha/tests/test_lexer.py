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
  
  def test_float(self):
    self.__testing_lexic('1.5', FLOAT)
    
  def test_str(self):
    self.__testing_lexic('"some text"', STRING)
    
  def test_char(self):
    self.__testing_lexic("'c'", CHAR)
    
  def test_eof(self):
    self.__testing_lexic('\n', EOF)
    
  def test_func_kw(self):
    self.__testing_lexic("func", FUNC_KW)
    
  def test_data_kw(self):
    self.__testing_lexic("data", DATA_KW)
    
  def test_name(self):
    self.__testing_lexic("somevar", NAME)
    self.__testing_lexic("someVar", NAME)
    self.__testing_lexic("SomeVar", NAME)
    self.__testing_lexic("some_var", NAME)
    self.__testing_lexic("_some_var", NAME)
    self.__testing_lexic("some_var2", NAME)

  def test_l_bracet(self):
    self.__testing_lexic('(', L_BRACET)
    
  def test_r_bracet(self):
    self.__testing_lexic(')', R_BRACET)
    
  def test_l_brace(self):
    self.__testing_lexic('{', L_BRACE)
    
  def test_r_brace(self):
    self.__testing_lexic('}', R_BRACE)
    
  def test_comma(self):
    self.__testing_lexic(',', COMMA)
 
 def