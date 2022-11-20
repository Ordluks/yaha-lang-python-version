import re
from compiler.data import *


lexic_rules = [
  LexicRule(EOF, r'\n'),
  LexicRule(None, r'[\s\t]'),
  LexicRule(None, r'\/\/.*$'),
  LexicRule(FLOAT, r'[0-9]+\.[0-9]+'),
  LexicRule(INTEGER, r'[0-9]+'),
  LexicRule(STRING, r'"[^"]*"'),
  LexicRule(CHAR, r"'[^']'"),
  LexicRule(FUNC_KW, r'func'),
  LexicRule(DATA_KW, r'data'),
  LexicRule(NAME, r'[a-zA-Z_]+[a-zA-Z0-9_]+'),
  LexicRule(L_BRACET, r'\('),
  LexicRule(R_BRACET, r'\)'),
  LexicRule(L_BRACE, r'{'),
  LexicRule(R_BRACE, r'}'),
  LexicRule(COMMA, r','),
  LexicRule(EQUAL, r'=')
]


def lexer(source, raise_error):
  def unexpected_char_error(char):
    raise_error(f'Unknown character "{char}"')
  
  def match_token(source, rules):
    if len(rules) == 0:
      unexpected_char_error(source[0])
    
    rules_copy = rules.copy()
    rule = rules_copy[0]
    
    result = re.match(rule.regexp, source)
    if result is None:
      return match_token(source, rules_copy[1:])
    else:
      return Token(rule.token_type, result.group(0))
  
  def lexing(source, tokens_acc=None):
    if len(source) == 0:
      return tokens_acc
    
    if tokens_acc is None:
      tokens_acc = []
      
    tokens_acc_copy = tokens_acc.copy()
    token = match_token(source, lexic_rules)
    if token.token_type is not None:
      tokens_acc_copy.append(token)
    
    return lexing(source[len(token.value):], tokens_acc_copy)
  
  return lexing(re.sub(r'\r\n|\r', '\n', source))
