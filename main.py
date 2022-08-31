# Biblioteca do python que permite utilizar expressões regulares (Regular Expressions)
import re

# Lista do nome dos tokens

def listaTokens(info):
    for i in str(info):
        if i == "(":
            print(f'A entrada "{i}" é o token AP')
        elif i == ")":
            print(f'A entrada "{i}" é o token FP')
        elif i == "+":
            print(f'A entrada "{i}" é o token SOM')
        elif i == "-":
            print(f'A entrada "{i}" é o token SUB')
        elif i == "*":
            print(f'A entrada "{i}" é o token MUL')
        elif i == "/":
            print(f'A entrada "{i}" é o token DIV')
        elif i == " ":
            continue
        elif re.search("0|1|2|3|4|5|6|7|8|9", i):
            print(f'A entrada "{i}" é um token NUM')
        else:
            print (f'A entrada "{i}" não é um token válido')
    return ("Análise concluida")


# Teste do campo de batalha
entrada = "amogus = 2+2"

print (listaTokens(entrada))
