import os
os.system("cls")

# 04 Contando valores pares e ímpares
# Use a lista n u m e r o s = [ 1 2 , 7 , 9 , 2 0 , 3 1 , 4 4 , 1 8 , 5 ] . Percorra os valores com for e conte
# quantos são pares e quantos são ímpares. Mostre as duas quantidades ao final.
# Recursos sugeridos: f o r , i f , % , c o n t a d o r e s e p r i n t ( )

numeros = [ 12 , 7 , 9 , 20 , 31 , 44 , 18 , 5, 0]
quantiadade = len(numeros)
pares = 0
impar = 0

for i in range(quantiadade):
    if (numeros[i] % 2 == 0 ):
        pares += 1
    else:
        impar += 1
    
print(f"Impares : {impar}")
print(f"Pares : {pares}")
