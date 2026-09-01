import os, time

os.system("cls")

# 03 Análise de números
# Peça seis números inteiros utilizando um laço for e armazene-os em uma lista. Depois, mostre a
# soma, o maior valor, o menor valor e os números em ordem crescente.
# Recursos sugeridos: f o r , i n t ( ) , a p p e n d ( ) , s u m ( ) , m a x ( ) , m i n ( ) e s o r t ( )

numeros = []
for i in range(6):
    numero = int(input(f"Digite o {i+1} número: "))
    numeros.append(numero)
    os.system("cls")
    
somaNumeros = sum(numeros)
maiorNumeros = max(numeros)
menorNumeros = min(numeros)
numeros.sort()

print("Relatório dos numeros informados! ")
print(f"Soma de todos os números: {somaNumeros}")
print(f"Maior número digitado:  {maiorNumeros}")
print(f"Menor número digitado: {menorNumeros}")
print(f"Numeros em ordem crescente: {numeros}")
    