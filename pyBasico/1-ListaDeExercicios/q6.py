import os,time
os.system("cls")

# 06 Menu de gerenciamento de tarefas
# Crie uma lista vazia e apresente continuamente o menu: 1 - Adicionar tarefa, 2 - Remover tarefa,
# 3 - Mostrar tarefas e 0 - Sair. Use w h i l e T r u e para manter o menu ativo, append() para
# adicionar, remove() para retirar e break para encerrar.
# Recursos sugeridos: w h i l e T r u e , i f / e l i f , a p p e n d ( ) , r e m o v e ( ) , p r i n t ( ) e b r e a k

tarefas = []
while True:
    print("\n-- Menu --")
    print("1 - Adicionar Tarefa")
    print("2 - Remover Tarefa")
    print("3 - Mostrar Tarefas")
    print("0 - Sair")
    op = int(input("Escolha uma opção: "))
    
    if (op == 1):
        tarefa = str(input("Informe a tarefa: "))
        tarefas.append(tarefa)
        print("Tarefa adicionada com sucesso!")
        time.sleep(1)
    elif (op == 2):
        quant = len(tarefas)
        print("As tarefas cadastradas são: ")
        for i in range(quant):
            print(tarefas[i])
        
        tarefaParaRemover = str(input("Qual tarefa deseja remover? "))
        if (tarefaParaRemover in tarefas):
            tarefas.remove(tarefaParaRemover)
            print(f"Tarefa removida com sucesso!")
        else:
            print("Tarefa não cadastrada!")
            
    elif(op == 3):
        quant = len(tarefas)
        print("As tarefas cadastradas são: ")
        if (quant != 0):
            for i in range(quant):
                print(tarefas[i])
        else:
            print("Não existem tarefas cadastradas!")
                
    elif (op !=0 ):
        print("Opção indisponível!")
        
    else:
        print("Encerrando...")
        break
        
        
        
