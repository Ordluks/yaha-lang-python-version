import os, sys
from compose import compose


def __show_error(msg):
  print(msg)
  sys.exit()

def __check_path(path):
  if not os.path.exists(path):
    __show_error(f'File not exists - {path}')
  else:
    return path


def __read_file(path):
  try:
    file = open(path, 'r')
    return file.read()
  except Exception:
    __show_error(f'Can not read file - {path}')


read = compose(__read_file, __check_path, os.path.abspath)
