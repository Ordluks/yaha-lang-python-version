from compiller.data import *
from errors import unexpected_syntax_error, unexpected_eof_error


def parser(tokens):
  def next_token():
    if len(tokens) == 0:
      unexpected_eof_error()
    return tokens.pop(0)
  
  def expect(*types):
    token = next_token()
    if token.token_type in types:
      return token
    else:
      unexpected_syntax_error(token.value)
  
  def where(func, *types):
    token = expect(*types)
    return func(token)
  
  def variants(cases):
    token = next_token()
    func = cases.get(token.token_type, None)
    if func is None:
      unexpected_syntax_error(token.value)
    else:
      return func(token.value)
      
  def until(token_type, func):
    nodes = []
    while tokens[0].token_type != token_type:
      nodes.append(func())
    
    next_token()
    return nodes
  
  
  def parse_root():
    functions_nodes = []
  
    while len(tokens) > 0:
      node = where(parse_function, FUNC_KW)
      functions_nodes.append(node)
      
    return RootNode(functions_nodes)
  
  def parse_function(_):
    name = expect(NAME)
    statement = parse_statement()
    return FunctionNode(name, statement)
  
  def parse_statement():
    expect(L_BRACE)
    nodes = until(R_BRACE, parse_line)
    return StatementNode([])
    
  def parse_line():
    return variants({
      STRING: lambda t : ExpressionNode(),
      DATA_KW: parse_data
    })
    
  def parse_data(_):
    name = expect(NAME)
    expect(EQUAL)
    return DataNode(name, parse_line())
    
    
  return parse_root()
