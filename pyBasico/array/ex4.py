import os
os.system("cls")

# 3) Escreva um programa que leia uma lista de 5 nomes e depois exiba esses
# nomes em ordem alfabética.
nomes = []

for i in range(5):
    nome = str(input("Digite um nome: "))
    nomes.append(nome)
    

os.system("cls")
print("Nomes em ordem alfabética: ")
print(nomes.sort())

    