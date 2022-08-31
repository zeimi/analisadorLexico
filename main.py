# Biblioteca do python que permite utilizar expressões regulares (Regular Expressions)
import re

# Lista do nome dos tokens

def listaTokens(info):
    for i in str(info):
        if i == "(":
            print(f'O token "{i}" é AP')
        elif i == ")":
            print(f'O token "{i}" é FP')
        elif i == "+":
            print(f'O token "{i}" é SOM')
        elif i == "-":
            print(f'O token "{i}" é SUB')
        elif i == "*":
            print(f'O token "{i}" é MUL')
        elif i == "/":
            print(f'O token "{i}" é DIV')
        elif i == " ":
            continue
        elif re.search("0|1|2|3|4|5|6|7|8|9", i):
            print(f'O token "{i}" é NUM')
        else:
            print (f'O vagabundo "{i}" não é valido')
    return ("Analise concluida")


# Teste do campo de batalha
entrada = "y = x/2"

print (listaTokens(entrada))
