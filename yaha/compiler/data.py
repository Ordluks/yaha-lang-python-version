# Lexing

class LexicRule:
  def __init__(self, token_type, regexp):
    self.token_type = token_type
    self.regexp = regexp


class Token:
  def __init__(self, token_type, value):
    self.token_type = token_type
    self.value = value


EOF = 'eof'
INTEGER = 'integer'
FLOAT = 'float'
STRING = 'string'
CHAR = 'char'
FUNC_KW = 'func_kw'
DATA_KW = 'data_kw'
NAME = 'name'
L_BRACET = 'l_bracet'
R_BRACET = 'r_bracet'
L_BRACE = 'l_brace'
R_BRACE = 'r_brace'
COMMA = 'comma'
EQUAL = 'equal'


lexic_rules = [
  LexicRule(None, r'[\s\t]'),
  LexicRule(None, r'\/\/.*$'),
  LexicRule(EOF, r'\n'),
  LexicRule(INTEGER, r'[0-9]+'),
  LexicRule(FLOAT, r'[0-9]+\.[0-9]+'),
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



# Parsing

EXPECT_ACTION_NAME = 'expect'
CASES_ACTION_NAME = 'cases'


class SyntaxRule:
  pass


class ExpressionNode:
  pass


class RootNode(ExpressionNode):
  def __init__(self, nodes):
    self.functions = nodes


class FunctionNode(ExpressionNode):
  def __init__(self, name, statement):
    self.name = name
    self.statement = statement


class StatementNode(ExpressionNode):
  def __init__(self, nodes):
    self.nodes = nodes


class DataNode(ExpressionNode):
  def __init__(self, name, node):
    self.name = name
    self.node = node
