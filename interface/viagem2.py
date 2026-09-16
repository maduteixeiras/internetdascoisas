import customtkinter as ctk

ctk.set_appearance_mode('dark')

# Funções
def calcular_gasto():
    try:
        # Substitui vírgula por ponto para evitar erros com números decimais
        d = float(distancia.get().replace(',', '.'))
        c = float(consumo.get().replace(',', '.'))
        pC = float(precoCombustivel.get().replace(',', '.'))
        
        # Evita divisão por zero se o consumo for digitado como 0
        if c == 0:
            resultado.configure(text='O consumo não pode ser 0!', text_color='red')
            return
            
        formula = (d / c) * pC
        resultado.configure(text=f'O valor para a viagem é de R$ {formula:.2f}', text_color='white')
        
    except ValueError:
        # Mensagem caso o usuário digite letras ou deixe campos vazios
        resultado.configure(text='Por favor, digite apenas números!', text_color='red')

# Janela
janela = ctk.CTk()
janela.geometry('500x550') # Aumentado levemente para acomodar o texto de erro sem cortar
janela.resizable(False, False)
janela.title('Calculadora de viagem')

# O try evita que o app quebre caso você mude o script de pasta e ele não ache o ícone
try:
    janela.iconbitmap('interface/aviao.ico')
except:
    pass

# Label - Título
titulo = ctk.CTkLabel(janela, text='APP VIAGEM', text_color='white', font=('Verdana', 50))
titulo.pack(pady=30)

# Entry - Distancia
distancia = ctk.CTkEntry(janela, placeholder_text='Digite a distancia da viagem em KM:', border_width=1, border_color='white', width=400, height=40)
distancia.pack(pady=15)

# Entry - Consumo
consumo = ctk.CTkEntry(janela, placeholder_text='Digite o consumo do seu veículo (KM/L)', border_color='white', border_width=1, width=400, height=40)
consumo.pack(pady=15)

# Entry - Preço Combustível
precoCombustivel = ctk.CTkEntry(janela, placeholder_text='Digite o preço atual do combustível', border_color='white', border_width=1, width=400, height=40)
precoCombustivel.pack(pady=15)

# Button - Calcular
# Correção: Mudado o nome da variável para 'btn_calcular' para não chocar com a função
btn_calcular = ctk.CTkButton(janela, text='Calcular gasto', cursor='hand2', width=150, height=40, fg_color='pink', text_color='black', command=calcular_gasto)
btn_calcular.pack(pady=20)

# Resultado
resultado = ctk.CTkLabel(janela, text='', font=('arial', 20), wraplength=450)
resultado.pack(pady=10)

janela.mainloop()
