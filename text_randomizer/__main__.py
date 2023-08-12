from .tokenizer import Tokenizer
from .lexer import Lexer
from .parser import Parser


source = '''Привет [1|2|3] fdsaf [+, +1|2|3] nfihdsi {{1|2|3}|{1|2|{9|8}}}'''


tokenizer = Tokenizer(source)
tokens = tokenizer.get_tokens()

lexer = Lexer(tokens)
lexemes = lexer.get_lexems()

parser = Parser(lexemes)
ast = parser.get_ast()
