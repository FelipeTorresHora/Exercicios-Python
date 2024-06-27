from cod_fun import *

print("############ Seja Bem-Vindo ############")
print("1 - Inverter Palavra\n2 - Mostrar maior numero aleaório\n3 - Maior palavra da lista")
while True:
    ope = input("Digite o numero da função que você quer acessar: ")
    if ope == "1":
        inverter(palavras)
        break
    elif ope == "2":
        print(mostrar_maior_num(10,2))
        break
    elif ope == "3":
        print(maior_palavra())
        break
    else:
        print("Operação Inválida")
