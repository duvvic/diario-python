def maior_numero(*numeros):
    return max(numeros)

numeros_salvos = []
tentativas = 0

while tentativas <3:
    entrada = input("Digite um número: ")
    try:
        numero_entrada = int(entrada)
        numeros_salvos.append(numero_entrada)
        tentativas += 1
    except ValueError:
        print('Isso não é um numero válido') 

if numeros_salvos:
    print("O MAIOR numero: ",maior_numero(*numeros_salvos))
else:    
    print("Lista vazia, adicione algum número primeiro.")


# Aqui fazemos que o usuario digite 3 vez um numero e ao final o programa mostra qual é o maior.
# e caso o usuario venha a digitar alguma string, aparecera para tentar novamente sem contabilizar no loop.
