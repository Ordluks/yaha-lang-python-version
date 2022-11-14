import re
from compiller.data import lexic_rules, Token
from errors import unexpected_char_error


def lexer(source):
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
