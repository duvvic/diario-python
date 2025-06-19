import os

def listar_diretorio():
    itens = os.listdir()
    for item in itens:
        print(item)



listar_diretorio()
