import os, time
os.system("cls")

# 02 Cadastro de cinco produtos
# Crie uma lista vazia. Utilize for com range(5) para pedir cinco produtos ao usuário e adicionar
# cada um com append() . Ao final, exiba a lista completa e a quantidade de produtos cadastrados.
# Recursos sugeridos: f o r , r a n g e ( ) , i n p u t ( ) , a p p e n d ( ) e l e n ( )

produtos = []

for i in range(5):
    produto = str(input(f"Digite o {i+1}° produto: "))
    produtos.append(produto)
    

os.system("cls")

print("Os produtos digitados foram: ")
for i in range(5):
    print(produtos[i])