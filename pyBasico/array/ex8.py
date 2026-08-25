import os
os.system("cls")

# 6) Filtragem e Média de Dados (Processamento de Vetores)
# Enunciado: Desenvolva um programa que peça ao usuário para digitar a nota de 8
# alunos e armazene-as em uma lista. O programa deve:
# 1. Calcular e mostrar a média aritmética da turma.
# 2. Criar e exibir uma nova lista contendo apenas as notas que ficaram acima
# da média calculada.

notas = []

for i in range(8):
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))
    notas.append(nota)


media = sum(notas) / len(notas)
print(f"\nMédia da turma: {media}")

# Verificando as notas
acima_media = []

for nota in notas:
    if nota > media:
        acima_media.append(nota)

print("\nNotas acima da média:")
print(acima_media)
