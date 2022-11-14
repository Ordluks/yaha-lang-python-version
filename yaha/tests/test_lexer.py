import unittest
from compiller.lexer import lexer
from compiller.data import *


class TestLexer(unittest.TestCase):
  def assertTokens(self, tokens1, tokens2):
    vars_list1 = list(map(vars, tokens1))
    vars_list2 =list(map(vars, tokens2))
    print('\n',vars_list1)
    self.assertTrue(vars_list1 == vars_list2)
    
  def test_error(self):
    with self.assertRaises(SystemExit):
      lexer('$$$')
  
  def test_int(self):
    int1 = '40'
    int2 = '648'
    tokens = lexer(f'{int1} {int2}')
    
    self.assertTokens(tokens, [
      Token(INTEGER, int1),
      Token(INTEGER, int2)
    ])
  
  def test_string(self):
    str1 = 'hello'
    str2 = 'world'
    tokens = lexer(f'"{str1}""{str2}"')
    
    self.assertTokens(tokens, [
      Token(STRING, f'"{str1}"'),
      Token(STRING, f'"{str2}"')
    ])
  
  def test_char(self):
    char1 = "'a'"
    char2 = "'b'"
    tokens = lexer(f'{char1}{char2}')
    
    self.assertTokens(tokens, [
      Token(CHAR, char1),
      Token(CHAR, char2)
    ])
    
  def test_name(self):
    name1 = 'some_name'
    name2 = 'someName'
    tokens = lexer(f'{name1} {name2}')
    
    self.assertTokens(tokens, [
      Token(NAME, name1),
      Token(NAME, name2)
    ])
    
  def test_kewords(self):
    tokens = lexer('func')
    self.assertTokens(tokens, [Token(FUNC_KW, 'func')])
