import os
import string
import pandas as pd

col = 0
linha = 0
estado = 0
palavra = []
erros = []
lexemacompleto = 0

tabela = pd.DataFrame(columns=['Classe', 'Lexema', 'Tipo'])
path_arquivo_fonte = os.path.join(os.path.dirname(__file__), 'FONTE.ALG')

arquivo_fonte = open(path_arquivo_fonte, mode='r', encoding='utf-8')

letras = list(string.ascii_letters)
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
reservadas = ['inicio', 'varinicio', 'varfim', 'escreva', 'leia', 'se', 'entao', 'fimse', 'Repita', 'fimRepita', 'fim', 'inteiro', 'literal', 'real']
estados_finais = pd.read_csv('Automato.csv')

#Scanner

for i in arquivo_fonte.read():
    col += 1
    palavra.append(i)
    if(i == '\n'):
        col = 0
        linha += 1
    if(estado==0):
        if(i in numeros):
            estado = 1
        elif(i in letras):
            estado = 9
        elif(i == '{'):
            estado = 10
        elif(i=='\"'):
            estado = 7
        elif(i=='<'):
            estado = 13
        elif(i=='>'):
            estado = 17
        elif(i=='='):
            estado = 19
        elif(i=='('):
            estado=20
        elif(i==')'):
            estado=21
        elif(i==';'):
            estado=22
        elif(i==','):
            estado=23
        elif(i=='+' or i=='-' or i=='*' or i=='/'):
            estado=24
        elif(i==' ' or i=='\n' or i=='\t'):
            estado=0
        else:
            lexemacompleto=1
    if(estado==1):
        if(i in numeros):
            estado = 1
        elif(i == '\.'):
            estado = 2
        else:
            lexemacompleto = 1
    if(estado == 9):
        if(i in letras):
            estado=9
        else:
            lexemacompleto=1

    if(lexemacompleto == 1):
        next = palavra.pop()
        lexema = ''.join(palavra)
        if(estado in estados_finais['estado'].values and lexema not in reservadas):
            df1 = pd.DataFrame({
                'Classe': [estados_finais.loc[estado][1]],
                'Lexema': [lexema],
                'Tipo': [estados_finais.loc[estado][3]]
                })
            tabela = pd.concat([tabela,df1], ignore_index = True)
        elif(lexema in reservadas):
            df1 = pd.DataFrame({
                'Classe': [lexema],
                'Lexema': [lexema],
                'Tipo': [lexema]
                })
            tabela = pd.concat([tabela,df1], ignore_index = True)
        else:
            df1 = pd.DataFrame({
                'Classe': ['ERRO'],
                'Lexema': [lexema],
                'Tipo': ['None']
                })
            tabela = pd.concat([tabela,df1], ignore_index = True)
            erros.append(f'ERRO léxico, Caractere inválido na linguagem.\n Linha {linha}, coluna {col} .')
        estado = 0
        lexema = ''
        lexemacompleto = 0
        palavra = []
        if(next!=" " or next!="\n" or next!="\t"):
            palavra.append(str(next))

print(tabela)
