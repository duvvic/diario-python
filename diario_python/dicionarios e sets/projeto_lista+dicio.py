#PROJETO FINALIZADO (AULA DE PYTHON)


#1 - Adicionar produto
#2 - Remover produto
#3 - Listar produtos
#4 - sair

estoque = []


while True:
    print("=="*20)
    print('GERENCIADOR DE ESTOQUE')
    print("=="*20)
    
    print( """
            1 - cadastrar produto
            2 - Remover produto
            3 - Listar produtos
            4 - sair\n
          """  )
    escolha = int(input('Escolha uma opção númerica: '))


    # if escolha == 1:
    #     addProduto = input('Adicionar Produto: ')
    #     estoque.append(addProduto) 
    #     print(f'\nPronto, produto {addProduto} adicionado.\n')  

    if escolha == 1:
        produto = {
            "nome":input('Nome produto: '),
            "preco":input('Preço produto: '),
            "quantidade":input('Quantidade produto: '),
                }
        estoque.append(produto) 
        print('\nPronto, produto criado.\n')


    elif escolha == 2:
        if not estoque:
            print('\nEstoque vazio. Nenhum produto para remover.\n')
            continue
        for produto in estoque:
            print(produto["nome"])
        remove = input('Remover produto: ') 
        try:
                estoque.remove(remove) 
                print(f'\nPronto, produto {remove} removido.\n')  
        except:
                print(f'\nERRO! Produto {remove}, NÃO encontrado.\n')


    elif escolha == 3:      
        for produto in estoque:
            for chave,valor in produto.items():
                print(f"{chave} = {valor}")
                print(f"="*10)
               

    elif escolha == 4:
        print('\nPrograma finalizado. Volte sempre.\n')
        break