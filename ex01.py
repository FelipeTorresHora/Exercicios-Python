#!/usr/bin/env python
# coding: utf-8

# In[9]:


"""
Faça um programa que solicite ao usuário que digite 10 valores para
preencher uma lista. Em seguida, o programa deve separar os números pares e ímpares em listas diferentes.
Por fim, exiba na tela os números pares, os números ímpares em uma tupla, a quantidade de números pares 
e ímpares presentes na lista, e a soma de todos os números pares e ímpares, respectivamente.
"""
numeros = []
par = []
impar = []
for i in range(10):
    numero = int(input("Digite um numero: "))
    numeros.append(numero)
    if numero % 2 == 0:
        par.append(i)
    elif numero % 2 != 0:
        impar.append(i)
par_t = tuple(par)
impar_t = tuple(impar)
print("Números pares:", par_t)
print("Números ímpares:", impar_t)
print("Quantidade de números pares:", len(par_t))
print("Quantidade de números pares:", len(impar_t))
print(sum(par))
print(sum(impar))

