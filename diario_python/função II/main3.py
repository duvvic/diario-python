#Ordenar por tamanho de string
#use sorted() com lambda para ordenar pela quantidade de letras.

lista_fruta = ['banana', 'uva', 'abacaxi', 'kiwi']
tamanho_palavra = sorted(lista_fruta, key=lambda lista_fruta: len(lista_fruta))

print(tamanho_palavra)
