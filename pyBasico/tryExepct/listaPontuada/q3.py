import os
os.system("cls")

print("-- Gerador de tabuada --")
while True:
    try:
        num = int(input("Informe o número: "))
        for i in range(11):
            print(f"{num} x {i} = {num * i}")
        break
    except ValueError:
        print("Erro: entrada inválida!")
        
