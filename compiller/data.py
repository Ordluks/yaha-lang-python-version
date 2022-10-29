# Lexing

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
FUNC_KW = 'func_kw'
NAME = 'name'
L_BRACET = 'l_bracet'
R_BRACET = 'r_bracet'
L_BRACE = 'l_brace'
R_BRACE = 'r_brace'
COMMA = 'comma'


lexic_rules = [
  LexicRule(None, r'[\s\t\n]'),
  LexicRule(None, r'\/\/.*$'),
  LexicRule(INTEGER, r'[0-9]+'),
  LexicRule(FLOAT, r'[0-9]+\.[0-9]+'),
  LexicRule(STRING, r'"[^"]*"'),
  LexicRule(CHAR, r"'[^']'"),
  LexicRule(FUNC_KW, r'func'),
  LexicRule(NAME, r'[a-zA-Z_]+[a-zA-Z0-9_]+'),
  LexicRule(L_BRACET, r'\('),
  LexicRule(R_BRACET, r'\)'),
  LexicRule(L_BRACE, r'{'),
  LexicRule(R_BRACE, r'}'),
  LexicRule(COMMA, r',')
]



# Parsing

EXPECT_ACTION_NAME = 'expect'
CASES_ACTION_NAME = 'cases'


class SyntaxRule:
  def __init__(self, node_class):
    self.node_class = node_class
    self.rule_descriptor = []
    self.until_token = None
    
  def add_to_rule_descriptor(self, action_name, data):
    rule_descriptor_copy = self.rule_descriptor.copy()
    step = (action_name, data)
    rule_descriptor_copy.append(step)
    self.rule_descriptor = rule_descriptor_copy
    return self
  
  def expect(self, *token_types):
    return self.add_to_rule_descriptor(EXPECT_ACTION_NAME, list(token_types))
  
  def require(self, token_type):
    return self.expect(token_type)
    
  def cases(self, cases_dict):
    return self.add_to_rule_descriptor(CASES_ACTION_NAME, cases_dict)
    
  def until(self, token_type):
    self.until_token = token_type


class ExpressionNode:
  def __init__(self, tokens, nodes):
    self.__tokens = tokens
    self.construct(tokens, nodes)
    
  def __len__(self):
    return len(self.__tokens)
    
  def construct(self, tokens, nodes):
    pass


class RootNode(ExpressionNode):
  def construct(self, tokens, nodes):
    self.functions = nodes


class FunctionNode(ExpressionNode):
  def construct(self)
  

syntax_rules = SyntaxRule(ExpressionNode) \
.expect(FUNC_KW) \
.require(NAME) \
.require(L_BRACET) \
.cases({
  NAME: SyntaxRule(ExpressionNode) \
  .expect(COMMA)
})

print(syntax_rules.rule_descriptor)
