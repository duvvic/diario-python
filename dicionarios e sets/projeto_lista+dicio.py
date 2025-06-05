#PROJETO FINALIZADO (AULA DE PYTHON)


#1 - Adicionar produto
#2 - Remover produto
#3 - Listar produtos
#4 - sair

estoque = []
def perguntar_continuar():
    resp = input("Deseja continuar? [s/n]: ").strip().lower()
    while resp not in ("s","n"):
        resp = input("Resposta inválida. Digite 's' para sim ou 'n' para não: ").strip().lower()
    return resp == "s"
        


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


    if escolha == 1:
        # produto = {
        #     "nome":input('Nome produto: '),
        #     "preco":input('Preço produto: '),
        #     "quantidade":input('Quantidade produto: '),
        #         }
        # estoque.append(produto) 
        # print('\nPronto, produto criado.\n')
        contador = 0
        AMARELO = "\033[33m"
        RESET = "\033[0m"
        #TENHO QUE TERMINAR ESSA FUNÇÃO DA OPÇÃO 1 ONDE TROCAR A SAIDA DE ESC POR OUTRA OPÇÃO.***************

        print(f"{AMARELO}Modo lote: digite 'esc' para voltar ao menu principal.{RESET}\n")

        while True:
            nome = input("Nome do produto: ").strip()
            # condição de saída:
            if nome.lower() == "esc":
                print(f"\nVocê cadastrou {contador} produto(s) nesta sessão.\n")
                break

             # pede preço e quantidade validando tipos
            try:
                preco = float(input("Preço do produto: "))
                quantidade = int(input("Quantidade do produto: "))
            except ValueError:
                print("⚠️  Preço ou quantidade inválidos. Tente novamente.\n")
                continue

            produto = {
                "nome": nome,
                "preco": preco,
                "quantidade": quantidade
            }
            estoque.append(produto)
            contador += 1
             # exibe contador atualizado
            print(f"{AMARELO}Total cadastrados nesta sessão:{RESET} {contador}\n")


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
        if not estoque:
             print("\nLista vazia. Nunhum item para listar.\n" ) 
        else:       
            for produto in estoque:
                for chave,valor in produto.items():
                    print(f"{chave} = {valor}")
                    print(f"="*10)
               

    elif escolha == 4:
        print('\nPrograma finalizado. Volte sempre.\n')
        break

    else:
         print("Opção invalida")

    if not perguntar_continuar():
        print("\nPrograma finalizado. Volte sempre.\n")
        break