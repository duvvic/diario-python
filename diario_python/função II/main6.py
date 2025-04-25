#Maior valor com *args
#Crie uma função que receba valores com *args e retorne o maior.

def maior_numero(*args):
    return max(args)

print(maior_numero(1,9,15,89,52,120,7))

#nessa função utilizamos o "max" para retornar o maior numero