import os
import customtkinter as ctk
ctk.set_appearance_mode('dark') # Configuração de aparência / cor

# Janela principal
janela = ctk.CTk()
janela.geometry('500x300')
janela.resizable(False, False)
janela.title('Sistema de acesso - 2026')
janela.iconbitmap('login.ico')



# Corpo da janela
titulo = ctk.CTkLabel(janela,
                    text= 'Sistema de Login',
                    text_color= '#297bff',
                    font=('arial',  50))
titulo.pack()



# Entrada de Login
login = ctk.CTkEntry(janela,
                    width=400,
                    height=40,
                    border_color='#297bff',
                    placeholder_text='Informe seu login:')
login.pack(pady=30)

# Entrada de senha
senha = ctk.CTkEntry(janela,
                    width=400,
                    height=40,
                    border_color='#297bff',
                    placeholder_text='Informe sua senha:',
                    show= '•')
senha.pack()


#  Botão de 'Acessar'
botao = ctk.CTkButton(janela,
                    width= 200,
                    height=40,
                    text= 'Acessar',
                    fg_color= '#297bff',
                    cursor = 'hand2')
                    
botao.pack(pady=30)




# ctkLabel = texto
# ctkEntry = caixa de entrada
# ctkButton = botão





janela.mainloop() # Loop principal