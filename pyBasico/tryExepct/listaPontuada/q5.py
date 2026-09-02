import os
os.system("cls")

while True:
    try:
        saldo = float(input("Informe o valor do saldo disponível: "))
        saque = float(input("Inform o valor do saque: "))
        
        if (saldo >= saque):
            print(f"Saque realizado com sucesso!")
            print(f"Valor restante: {saldo - saque}")
        else:
            print("O saque não pode ser realizado!")
            break
    except ValueError:
        print("Erro: entradas inválidas!")
        
        