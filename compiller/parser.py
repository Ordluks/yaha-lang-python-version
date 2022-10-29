from compiller.data import *
from errors import unexpected_syntax_error


def parser(tokens):
  def expect(token_types, token, tokens):
    if token.token_type in token_types:
      return True
    else:
      unexpected_syntax_error(token.value)
  
  def cases(cases_dict, token, tokens):
    expect(cases_dict.keys())
    parsing_case = cases_dict[token.token_type]
    return parsing(parsing_case, tokens)
  
  actions = {
    EXPECT_ACTION_NAME: expect
  }
  
  def match_node(rule, tokens):
    def matching(rule_descriptor, tokens, acc):
      if len(rule_descriptor) == 0 or len(tokens) == 0:
        return acc
        
      descriptor_copy = rule_descriptor.copy()
      step = descriptor_copy.pop(0)
      action_name = step[0]
      types_for_action = step[1]
      
      tokens_copy = tokens.copy()
      token = tokens_copy.pop(0)
      
      actions[action_name](types_for_action, token, tokens_copy)
      
      acc_copy = acc.copy()
      acc_copy.append(token)
      
      return matching(descriptor_copy, tokens_copy, acc_copy)
    
    scaned_tokens = matching(rule.rule_descriptor, tokens, [])
    print(list(map(vars, scaned_tokens)))
    return rule.node_class(scaned_tokens)
  
  def parsing(rule, tokens, node_acc=None):
    if len(tokens) == 0:
      return node_acc

    tokens_copy = tokens.copy()
    node = match_node(rule, tokens)
    
    return parsing(rule, tokens_copy[len(node):], node)
  
  return parsing(syntax_rules, tokens)
