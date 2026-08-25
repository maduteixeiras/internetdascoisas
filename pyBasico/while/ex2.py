import os
os.system("cls")


numeros = []

while True:
    num = float(input("Digite o número que você deseja armazenar: \nDigite 0 para para a execução\n"))
    if (num != 0):
        numeros.append(num)
    else:
        print(f"Numéros digitados: {numeros}")
        print(f"Soma dos numéros digitados: {sum(numeros)}")
        break
    
# 2) O Somador Infinito (while True + append)
# Crie um programa que peça números ao usuário indefinidamente.
# Se o usuário digitar 0, o programa para.
# Cada número digitado (exceto o 0) deve ser guardado em uma lista.
# No final, mostre a lista completa e a soma de todos os itens usando sum().