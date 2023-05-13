import os
import string
import numbers

path_arquivo_fonte = os.path.join(os.path.dirname(__file__), 'FONTE.ALG')

arquivo_fonte = open(path_arquivo_fonte, mode='r', encoding='utf-8')

letras = list(string.ascii_letters)
numeros = list(range(0,10))
simbolos = [
    ',', ';', ':', '.', '!', '?', '\\' , '*' ,'+' ,'-' , '/' , '(',
    ')', '{', '}', '[',']','<' , '>', '=', '\'', '“', '_'
    ]
palavras = ['inicio', 'varinicio', 'varfim', 'escreva', 'leia', 'se', 'entao', 'fimse', 'Repita', 'fimRepita', 'fim', 'inteiro', 'literal', 'real']
estados = list(range(0,24))
print(estados)