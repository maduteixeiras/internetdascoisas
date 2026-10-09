import customtkinter as ctk
ctk.set_appearance_mode('dark')


def calcularRes():
    qtdD = int(qtdDiarias)
    
    media = (n1 + n2) / 2
    if (media < 5):
        resultado.configure(text=f'Média: {media}\nSituação: Reprovado')
    elif (media >= 7):
        resultado.configure(text=f'Média: {media}\nSituação: Aprovado')
    else:
        resultado.configure(text=f'Média: {media}\nSituação: Recuperação')

janela = ctk.CTk()
janela.geometry('500x500')
janela.resizable(False, False)
janela.title('Reserva de Hotel')

labelNome = ctk.CTkLabel(janela, text='Nome do Hóspede:')
labelNome.pack(anchor='w', padx=25, pady=5)

nome = ctk.CTkEntry(janela, placeholder_text='Digite o nome do hóspede', text_color='white', width=400)
nome.pack(anchor='w', padx=25, pady=5)

labelQtdDiarias = ctk.CTkLabel(janela, text='Quantidade de Diárias:')
labelQtdDiarias.pack(anchor='w', padx=25, pady=5)

qtdDiarias = ctk.CTkEntry(janela, placeholder_text='Digite a quantidade de diárias:', text_color='white', width=400)
qtdDiarias.pack(anchor='w', padx=25, pady=5)

labelVDiaria = ctk.CTkLabel(janela, text='Valor da Diária (R$):')
labelVDiaria.pack(anchor='w', padx=25, pady=5)

vDiarias = ctk.CTkEntry(janela, placeholder_text='Digite o valor da diária:', text_color='white', width=400)
vDiarias.pack(anchor='w', padx=25, pady=5)

calcular = ctk.CTkButton(janela,
                            text='Calcular Hospedagem',
                            cursor = 'hand1',
                            width=60,
                            height=40,
                            fg_color='blue',
                            text_color='white',
                            command=calcular)
calcular.pack()
resultado = ctk.CTkLabel(janela,
                        text='',
                        font= ('arial', 30))

resultado.pack(pady=10)


janela.mainloop()