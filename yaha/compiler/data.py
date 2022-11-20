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
