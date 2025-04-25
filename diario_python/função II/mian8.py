# typr hint --> dica de tipo
def somar(a:int,b:int):
    return a + b


dobraValor = lambda x: x*2
lista_numeros = [2,4,5,6,7,8,9,11,50]
lista_numeros_dobrados = list(map(lambda x: x*2,lista_numeros))
lista_numeros_quadrado = list(map(lambda x: x*x,lista_numeros))
print(lista_numeros_quadrado)