import sys


def show_error(msg):
  print(msg)
  sys.exit()


def create_error_template(template):
  def error_type(info):
    msg = template + info
    show_error(msg)
  
  return error_type


def file_not_exists_error(path):
  show_error(f'File not exists - {path}')


def file_reading_error(path):
  show_error(f'Can not read file - {path}')


lexing_error = create_error_template('[LexerError] - ')


def unexpected_char_error(char):
  lexing_error(f'Unexpected character "{char}"')


parsing_error = create_error_template('[ParsingError] - ')


def unexpected_syntax_error(found_text):
  parsing_error(f'Unexpected syntax "{found_text}"')


def unexpected_eof_error():
  parsing_error('Unexpected end of line')
  