from compiler.steps import combine_steps
from compiler.lexer import lexer
from compiler.parser import parser


compiler = combine_steps(lexer, parser)
