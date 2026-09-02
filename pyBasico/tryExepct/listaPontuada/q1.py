import os, time
os.system("cls")

while True:
    try:
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        break
    except ValueError:
        print("Erro: digite apenas números!")
        


resultado = num1 + num2
print(f"\nO resultado é: {resultado}")
        