def dump_all(obj):
  if not hasattr(obj, '__dict__'):
    return obj

  obj_dict = vars(obj)
  result_dict = {}
  for key, value in list(obj_dict.items()):
    if isinstance(value, list):
      result_dict[key] = list(map(vars, value))
    else:
      result_dict[key] = dump_all(value)
  
  return result_dict
  