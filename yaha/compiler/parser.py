from compiler.data import *


def parser(tokens, raise_error):
  def syntax_error(text, expected):
    raise_error(f'Invalid syntax. Found "{text}", but "{expected}" was expected')
    
  def end_of_input_error():
    raise_error(f'Unexpected end of input')
  
  def end_of_line_error():
    raise_error('Invalid syntax.')
    
  
  def next_token():
    if len(tokens) == 0:
      end_of_input_error()
    return tokens.pop(0)
  
  def expect(token_type):
    token = next_token()
    
    if token.token_type == token_type:
      return token
    else:
      syntax_error(token.value, token_type)
  
  def where(func, token_type):
    token = expect(token_type)
    return func(token)
  
  def variants(cases):
    token = next_token()
    func = cases.get(token.token_type, None)
    if func is None:
      syntax_error(token.value, list(cases.keys())[0])
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
    expect(L_BRACET)
    expect(R_BRACET)
    statement = parse_statement()
    return FunctionNode(name, statement)
  
  def parse_statement():
    expect(L_BRACE)
    nodes = until(R_BRACE, parse_line)
    return StatementNode(nodes)
    
  def parse_line():
    node = parse_expr()
    
    if tokens[0].token_type == EOF:
      next_token()
      return node
    else:
      if tokens[0].token_type != R_BRACE:
        end_of_line_error()
      else:
        return node
      
  def parse_expr():
    return variants({
      STRING: lambda t : ExpressionNode(),
      DATA_KW: parse_data
    })

  def parse_data(_):
    name = expect(NAME)
    expect(EQUAL)
    return DataNode(name, parse_expr())
    
  return parse_root()
