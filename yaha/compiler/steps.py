import sys
from functools import partial


def create_error_rsiser(name):
  def raise_error(msg):
      print(f'({name.capitalize()}Error) - {msg}')
      sys.exit()
      
  return raise_error

def combine_steps(*steps):
  def run_steps(steps, arg):
    if len(steps) == 0:
      return arg
    steps_copy = steps.copy()
    step = steps_copy[0]
    step_name = step.__name__
    raise_error = create_error_rsiser(step_name)
    
    result = step(arg, raise_error)
    return run_steps(steps_copy[1:], result)
    
  return partial(run_steps, list(steps))
 