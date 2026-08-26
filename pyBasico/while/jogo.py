import random

acertos = 0
erros = 0


jogadas = int(input("Quantas vezes deseja jogar? "))
for i in range(jogadas):
    numeroSecreto = random.randint(1, 100)
    tentativas = 0

    print(f"\nPartida {i+1}")

    while True:
        numeroTentado = int(input("Digite um número: - 0 para parar o jogo \n"))
        tentativas += 1

        if (numeroTentado == numeroSecreto):
            acertos += 1
            print(f"Você acertou em {tentativas} tentativas!")
            break
        if (numeroTentado == 0):
            tentativas -= 1
            break
        elif numeroTentado < numeroSecreto:
            erros += 1
            print("O número secreto é maior.")
        else:
            erros += 1
            print("O número secreto é menor.")
        

    print("\nInformações da partida:")
    print(f"Tentativas: {tentativas}")
    print(f"Acertos: {acertos}")
    print(f"Erros: {erros}")
