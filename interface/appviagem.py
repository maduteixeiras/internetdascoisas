import customtkinter as ctk
ctk.set_appearance_mode('dark')



# Funcões
def calcular():
    d = int(distancia.get())
    c = int(consumo.get())
    pC = float(precoCombustivel.get())
    
    formula = (d/c) * pC
    
    resultado.configure(text=f'O valor para a viagem é de R$ {formula:.2f}')
    
# Janela
janela = ctk.CTk()
janela.geometry('500x500')
janela.resizable(False,False)
janela.title('Calculadora de viagem')
janela.iconbitmap('interface/aviao.ico')
# ---


# Label - Título
titulo = ctk.CTkLabel(janela,
                    text= 'APP VIAGEM',
                    text_color= 'white',
                    font= ('Verdana', 50))
titulo.pack(pady=30)
# ---


# Entry - Distancia
distancia = ctk.CTkEntry(janela,
                        placeholder_text= 'Digite a distancia da viagem em KM:' ,
                        border_width= 1,
                        border_color= 'white',
                        width= 400,
                        height= 40
                        )
distancia.pack(pady=30)
# ---

# Entry - Consumo
consumo = ctk.CTkEntry(janela,
                    placeholder_text= 'Digite o consumo do seu veículo',
                    border_color= 'white',
                    border_width= 1,
                    width=400,
                    height=40
                    )
consumo.pack()
# ---

# Entry - Preço Combustível
precoCombustivel = ctk.CTkEntry(janela,
                            placeholder_text= 'Digite o preço atual do combustível',
                            border_color= 'white',
                            border_width= 1,
                            width= 400,
                            height=40)
precoCombustivel.pack(pady=30)
# ---


# Button - Calcular
calcular = ctk.CTkButton(janela,
                        text='Calcular gasto',
                        cursor = 'hand2',
                        width= 60,
                        height= 40,
                        fg_color= 'pink',
                        text_color= 'black',
                        command=calcular
                        # border_width= 1,
                        # border_color= 'red'
                        )
calcular.pack()
# ---


resultado = ctk.CTkLabel(janela,
                        text='',
                        font= ('arial', 30))

resultado.pack(pady=10)

janela.mainloop()



