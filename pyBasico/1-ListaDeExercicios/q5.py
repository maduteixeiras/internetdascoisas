import os
os.system("cls")

# 05 Lista de convidados com palavra de saída
# Crie uma lista vazia e utilize w h i l e T r u e para receber nomes. Cada nome deve ser incluído com
# append() . Quando o usuário digitar 'fim' , encerre com break . Depois, organize os nomes em
# ordem alfabética e mostre a lista e sua quantidade.
# Recursos sugeridos: w h i l e T r u e , i n p u t ( ) , i f , b r e a k , a p p e n d ( ) , s o r t ( ) e l e n ( )

convidados = []

while True:
    convidado = input("Digite o nome do convidado (0 para encerrar): ")

    if convidado == "0":
        quant = len(convidados)

        print("Os convidados informados são:")
        for i in range(quant):
            print(convidados[i])
        break

    else:
        convidados.append(convidado)
