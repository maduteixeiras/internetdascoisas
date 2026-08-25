import os
os.system("cls")

# 5) Validação de Dados com Laço Indeterminado (Estruturas de Repetição)
# Enunciado: Escreva um programa que simule o cadastro de uma senha. O
# programa deve solicitar que o usuário digite uma senha de 4 dígitos numéricos.
# • Enquanto o usuário digitar uma senha que não tenha exatamente 4
# caracteres ou que não seja composta apenas por números, o programa
# deve exibir "Senha Inválida" e solicitar novamente.
# • Quando a senha for válida, exibir "Senha cadastrada com sucesso".
# Dica: Use while e a função len() para verificar o comprimento.

senha = []

sen = input("Digite uma senha de 4 dígitos: ")

while len(sen) != 4 or not sen.isdigit():
    print("Senha inválida")
    sen = input("Digite novamente: ")

senha.append(sen)
print("Senha cadastrada com sucesso!")
