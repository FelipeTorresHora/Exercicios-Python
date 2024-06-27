#!/usr/bin/env python
# coding: utf-8

# In[ ]:


""" Um exemplo de como os dados são extraidos de um arquivo csv"""
cadastro_csv = [
    "Maria, 28, Cientista de Dados",
    "João, 32, Desenvolvedor Frontend",
    "Jonas, 40, Desenvolvedor Backend",
    "Mauro, 38"
]
def processa_dados(cadastros):
""" 
Essa função tem como finalidade, separar os dados de cadastro, além de informar 
erro quando o formato dos dados vier incorreto e informar erro quando a idade for 
inserida com o tipo errado  
"""
    for cadastro in cadastros:
        dados = cadastro.split(",")
    
        if len(dados) != 3:
            raise ValueError("Formato incorreto dos dados")
        
        nome = dados[0]
        try:
            idade = int(dados[1])
        except ValueError:
            raise ValueError("Erro no formato do dado:'Idade'")  
        cargo = dados[2]
        print (f"{nome} tem {idade} anos e exerce o cargo de{cargo}")
try:
    processa_dados(cadastro_csv)
except ValueError as excecao:
    print(f"O programa encontrou um erro. Erro: {excecao}")
    

