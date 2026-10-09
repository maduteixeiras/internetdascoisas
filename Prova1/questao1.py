import customtkinter as ctk
ctk.set_appearance_mode('dark')



# Função para Calcular resultado
def calcularRes():
    n1 = float(nota1.get())
    n2 = float(nota2.get())
    
    media = (n1 + n2) / 2
    if (media < 5):
        resultado.configure(text=f'Média: {media}\nSituação: Reprovado')
    elif (media >= 7):
        resultado.configure(text=f'Média: {media}\nSituação: Aprovado')
    else:
        resultado.configure(text=f'Média: {media}\nSituação: Recuperação')
    
# Criando a Janela
janela = ctk.CTk()
janela.geometry('500x500')
janela.resizable(False,False)
janela.title('Resultado Acadêmico')
janela.iconbitmap()

# Label para o Nome do Aluno
labelNome = ctk.CTkLabel(janela,
                        text='Nome do Aluno:')
labelNome.pack(anchor = 'w', padx = 25, pady = 5 )
# Entry - Nome do ALuno
nomeALuno = ctk.CTkEntry(janela,
                        placeholder_text='Digite o nome do aluno',
                        text_color='white',
                        width=400)
                        
nomeALuno.pack(anchor = 'w', padx = 25, pady = 5)

# Lable para o Nota 1
labelNota1 = ctk.CTkLabel(janela,
                        text='Nota 1:')
labelNota1.pack(anchor = 'w', padx = 25, pady = 5 )
# Entry - Nota 1
nota1 = ctk.CTkEntry(janela,
                        placeholder_text='Digite a nota 1:',
                        text_color='white',
                        width=400)
                        
nota1.pack(anchor = 'w', padx = 25, pady = 5)

# Lable para o Nota 2
labelNota2 = ctk.CTkLabel(janela,
                        text='Nota 2:')
labelNota2.pack(anchor = 'w', padx = 25, pady = 5 )
# Entry - Nota 2
nota2 = ctk.CTkEntry(janela,
                        placeholder_text='Digite a nota 2:',
                        text_color='white',
                        width=400)
                        
nota2.pack(anchor = 'w', padx = 25, pady = 5)

# Button - Calacular resultado
calcularRes = ctk.CTkButton(janela,
                            text='Calcular Resultado',
                            cursor = 'hand1',
                            width=60,
                            height=40,
                            fg_color='blue',
                            text_color='white',
                            command=calcularRes)
calcularRes.pack()
resultado = ctk.CTkLabel(janela,
                        text='',
                        font= ('arial', 30))

resultado.pack(pady=10)


janela.mainloop()