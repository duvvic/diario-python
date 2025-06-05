#Contar argumentos numéricos com *args
#Crie uma função que diga quantos argumentos numéricos foram passados via *args.

def numeros(*args):
    return len(args)

print(numeros(1,2,8,6,5,4,5))

#nessa função estamos contando quantos elementos tem, utilizando "len(args)"