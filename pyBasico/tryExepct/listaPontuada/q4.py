import os
os.system("cls")

notas = []

while True:
    try:
        for i in range(3):
            nota = float(input(f"Informe a {i+1}° nota: "))
            notas.append(nota)
        break
    except ValueError:
        print("Erro: digite apenas números!")
        
os.system("cls")
media = sum(notas) / len(notas)
print("-- Resultado --")
print(f"Média: {media:.2f}")
if (media  < 5):
    print("Reprovado!")
elif (media < 7):
    print("Você está na recuperação!")
else:
    print("Aprovado!")
    