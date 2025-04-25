#Concatenar strings com *args
#Crie uma função que una todas as strings passages Como argumentos em uma única string separada por espaço.

def uniao (*args):
    return " ".join(args)

print(uniao('victor','almeida'))

#aqui nessa função estamos juntando as string do args em uma so linha. e utilizamos o " ".join(args) para dat espaço
#em cadda argumento e somente o valor da string. sem o "".join retornaria literalmente ('victor','almeida').