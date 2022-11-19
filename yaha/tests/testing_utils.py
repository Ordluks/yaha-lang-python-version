import json

def dump_all(obj):
  if not hasattr(obj, '__dict__'):
    return obj

  obj_dict = vars(obj)
  result_dict = {}
  result_dict['TYPE'] = obj.__class__.__name__
  
  for key, value in list(obj_dict.items()):
    if isinstance(value, list):
      result_dict[key] = list(map(dump_all, value))
    else:
      result_dict[key] = dump_all(value)
  
  return result_dict
  