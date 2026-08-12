import os
os.system('cls')

un1 = float(input('Digite a nota da 1° unidade: '))
un2 = float(input('Digite a nota da 2° unidade: '))
un3 = float(input('Digite a nota da 3° unidade: '))

media = (un1 + un2 + un3)/ 3

if (media >=5):
    print(f'Sua média foi {media:.1f}. Você foi aprovado!')
else:
    print(f'Sua média foi {media:.1f}. Você foi reprovado!')