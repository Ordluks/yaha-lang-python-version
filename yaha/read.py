import os
from compose import compose
from errors import file_not_exists_error, file_reading_error


def __check_path(path):
  if not os.path.exists(path):
    file_not_exists_error(path)
  else:
    return path


def __read_file(path):
  try:
    file = open(path, 'r')
    return file.read()
  except Exception:
    file_not_exists_error(path)


read = compose(__read_file, __check_path, os.path.abspath)
