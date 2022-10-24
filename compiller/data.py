class LexicRule:
  def __init__(self, token_type, regexp):
    self.token_type = token_type
    self.regexp = regexp


class Token:
  def __init__(self, token_type, value):
    self.token_type = token_type
    self.value = value


INTEGER = 'integer'
FLOAT = 'float'
STRING = 'string'
CHAR = 'char'
NAME = 'name'
FUNC_KW = 'func_kw'
L_BRACET = 'l_bracet'
R_BRACET = 'r_bracet'
L_BRACE = 'l_brace'
R_BRACE = 'r_brace'


lexic_rules = [
  LexicRule(None, r'[\s\t\n]'),
  LexicRule(None, r'\/\/.*$'),
  LexicRule(INTEGER, r'[0-9]+'),
  LexicRule(FLOAT, r'[0-9]+\.[0-9]+'),
  LexicRule(STRING, r'"[^"]*"'),
  LexicRule(CHAR, r"'[^']'"),
  LexicRule(NAME, r'[a-zA-Z_]+[a-zA-Z0-9_]+'),
  LexicRule(FUNC_KW, r'func'),
  LexicRule(L_BRACET, r'('),
  LexicRule(R_BRACET, r')'),
  LexicRule(L_BRACE, r'{'),
  LexicRule(R_BRACE, r'}')
]
