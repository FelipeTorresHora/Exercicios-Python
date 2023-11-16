#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def somar(n1: float,n2: float) -> float:
    """ Função para somar dois numeros """
    return(n1+n2)
def subtrair(n1: float,n2: float) -> float:
    """ Função para subtrair dois numeros """    
    return(n1-n2)
def mult(n1: float,n2: float) -> float:
    """ Função para multiplicar dois numeros """
    return(n1*n2)
def div(n1: float,n2: float) -> float:
    """ Função para dividir dois numeros """
    return(n1/n2)

while True:
""" Irá receber dois numeros e perguntar qual tipo de operaçao para ser feita """
    n1 = float(input("Digite o primeiro numero: "))
    n2 = float(input("Digite o segundo numero: "))
    ope = input("Qual tipo de operação: ")
""" A partir da operação digitada irá efetuar o código ou dizer o erro que aconteceu """
    if ope == "soma":
        print(somar(n1,n2))
    elif ope == "subtrair":
        print(subtrair(n1,n2))
    elif ope == "mult":
        print(mult(n1,n2))
    elif ope == "divisão":
        if n2 == 0:
            print("Não pode dividir por 0")
            break
        print(div(n1,n2))
    elif ope == "sair":
        break    
    else:
        print("Operação inválida. Tente novamente!")

