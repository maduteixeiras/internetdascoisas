import os
import random
os.system("cls")

# 2) Crie um programa em Python que lê uma lista de 10 nomes e sorteia um
# nome entre eles.

nomes = []

for i in range(10):
    nome = str(input(f"Digite o {i+1}° nome: "))
    nomes.append(nome)
    
os.system("cls")

nomeSorteado = random.choice(nomes)
print("O nome sorteado foi: ")
print(nomeSorteado)

