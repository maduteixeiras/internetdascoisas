while True:
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Por favor, digite apenas números válidos.")
        continue

    while True:
        operacao = input("Digite a operação (+, -, *, /): ")
        if operacao in ('+', '-', '*', '/'):
            break
        print("Operação inválida. Tente novamente.")

    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '/':
        if num2 != 0:
            resultado = num1 / num2
        else:
            print("Erro: Divisão por zero não é permitida.")
            continue

    print(f"O resultado é: {resultado}")