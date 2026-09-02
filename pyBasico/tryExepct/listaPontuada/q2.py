import os
os.system("cls")

while True:
    try:
        idade = int(input("Digite a sua idade: "))
        if (idade >= 18):
            print("Você é maior de idade!")
        else:
            print("Você é menor de idade!")
        break
    except:
        print("Erro: digite uma idade válida!")
        