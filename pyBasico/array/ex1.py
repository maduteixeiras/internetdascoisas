import os
os.system("cls")

temperatura = []

for i in range(5):
    temp = float(input(f"Digite a {i+1}° temperatura: "))
    temperatura.append(temp)
    

mediaTemp = sum(temperatura) / len(temperatura)
maiorTemp = min(temperatura)
menorTemp = max(temperatura)

os.system("cls")
print("Informações de temperaturas: ")
print(f"A média de temperaturas é: {mediaTemp}")
print(f"A maior temperatura foi: {maiorTemp:.1f}°C")
print(f"A menor temperatura foi: {menorTemp:.1f}°C")

# 1) Peça ao usuário para digitar 5 temperaturas (uma por uma) e guarde-as em uma lista.
# Use um laço para a entrada de dados.
# Após a leitura, exiba:
# A maior temperatura registrada (max).
# A menor temperatura registrada (min).
# A média das temperaturas.