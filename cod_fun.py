def inverter(palavra:str) -> str:
    """ Recebe uma palavra parâmetro e a retorna invertida"""
    palavras = input("Digite uma palavra: ")
    print (f"A sua palavra ao contrario é igual: {palavras[::-1]}")
def mostrar_maior_num(a:float, b:float) -> float:
    """ Recebe dois numeros e retorna o maior deles """
    if a > b:
        return f"O numero {a} é o maior"
    elif a == b:
        return "Os numeros são iguais"
    else:
        return f"O numero {b} é o maior"

def maior_palavra():
    """ Recebe uma lista de palavras e retorna a maior palavra da lista"""
    max = len(palavras[0])
    palavra = palavras[0]
    for i in palavras:
        if(len(i) > max):
            max = len(i)
            palavra = i
    return f"A maior palavra da sua lista é: {palavra}"
palavras = ["Brasil","Vitoria","Bahia","Salvador"]
