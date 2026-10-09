import customtkinter as ctk
ctk.set_appearance_mode('dark')

# Função para calcular o valor da hospedagem
def calcular():
    qtdD = int(qtdDiarias.get())
    vD = float(vDiarias.get())
    total = qtdD * vD
    resultado.configure(text=f'Total a pagar: R$ {total:.2f}')
    if (qtdD >= 5):
        resultado.configure(text = f'Hospedagem: {qtdD*vD:.2f} \nDesconto: {qtdD*vD*0.1:.2f} \nTotal a pagar: {(qtdD*vD)-(qtdD*vD*0.1):.2f}')
    else:
        resultado.configure(text = f'Hospedagem: {qtdD*vD:.2f} \nDesconto: 0.00 \nTotal a pagar: {qtdD*vD:.2f}')
    
# Criando a janela 
janela = ctk.CTk()
janela.geometry('500x500')
janela.resizable(False, False)
janela.title('Reserva de Hotel')

#  Label para o nome do hóspede
labelNome = ctk.CTkLabel(janela, text='Nome do Hóspede:')
labelNome.pack(anchor='w', padx=25, pady=5)
# Entry - nome do hgóspede 
nome = ctk.CTkEntry(janela, placeholder_text='Digite o nome do hóspede', text_color='white', width=400)
nome.pack(anchor='w', padx=25, pady=5)

# Label para a qtdDiarias
labelQtdDiarias = ctk.CTkLabel(janela, text='Quantidade de Diárias:')
labelQtdDiarias.pack(anchor='w', padx=25, pady=5)
# Entry - qtdDiarias
qtdDiarias = ctk.CTkEntry(janela, placeholder_text='Digite a quantidade de diárias:', text_color='white', width=400)
qtdDiarias.pack(anchor='w', padx=25, pady=5)

# Label para o vDiarias
labelVDiaria = ctk.CTkLabel(janela, text='Valor da Diária (R$):')
labelVDiaria.pack(anchor='w', padx=25, pady=5)
# Entry - vDiarias
vDiarias = ctk.CTkEntry(janela, placeholder_text='Digite o valor da diária:', text_color='white', width=400)
vDiarias.pack(anchor='w', padx=25, pady=5)

# Button - chamado para calcular o valor da hospedagem
calcular = ctk.CTkButton(janela,
                            text='Calcular Hospedagem',
                            cursor = 'hand1',
                            width=60,
                            height=40,
                            fg_color='blue',
                            text_color='white',
                            command=calcular)
calcular.pack()
# Label - mostrar o resultado do valor da hospedagem com a função calcular
resultado = ctk.CTkLabel(janela,
                        text='',
                        font= ('arial', 30))

resultado.pack(pady=10)


janela.mainloop()