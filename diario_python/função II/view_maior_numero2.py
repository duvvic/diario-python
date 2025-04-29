def maior_numero(*numeros):
    return max(numeros)

numeros_salvos = []

while True:
    # Aqui esta o ponto de partida ---->>>
    entrada = input("Digite um número ('s' mostrar): ")
    # End
    if entrada == "s":
        if numeros_salvos:
            print("O MAIOR numero: ",maior_numero(*numeros_salvos))
            break
        else:    
            print("Lista vazia, adicione algum número primeiro.")    
    else:
        try:
            numero_usuario = int(entrada)
            numeros_salvos.append(numero_usuario)
        except ValueError:
            print('Isso não é um numero válido.')


#Esse aqui é um programa que retorna o maior numero inserido na "entrada" e essa entrada pode ser
#transportada de outro lugar. 
