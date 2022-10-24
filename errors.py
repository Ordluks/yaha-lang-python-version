import sys


def show_error(msg):
  print(msg)
  sys.exit()

def unexpected_char_error(char):
  show_error(f'[LexerError] - Unexpected character "{char}"')
