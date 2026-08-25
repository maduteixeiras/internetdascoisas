import os
os.system("cls")

# Questão:
# 1) Crie um programa que lê uma lista de 10 números e conta a quantidade de
# números positivos e a quantidade de números negativos, e mostra o vetor
# com os negativos e o a soma dos positivos?

numerosPositivos = []
numerosNegativos = []
neutros = []


for i in range(10):
    num = float(input(f"Digite o {i+1}° número: "))
    if (num > 0):
        numerosPositivos.append(num)
    elif (num < 0 ):
        numerosNegativos.append(num)
    else:
        neutros.append(num)
        

os.system("cls")
print("Informações: ")
print(f"Quantidader de números positivos: {len(numerosPositivos)}")
print(f"Numeros negativos: {len(numerosNegativos)}")
print(f"Números iguais a 0: {len(neutros)}")
print(f"Soma dos números positivos: {sum(numerosPositivos)}")
soma = sum(numerosNegativos) + sum(numerosPositivos)
print(f"Soma de todos os números digitados: {soma}")
