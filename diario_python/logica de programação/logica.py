#[PYIA-A03] 

produtos = {}
n = 0

while n in range(5):
   produto = input('produto: ')
   preco = float(input('R$: '))
   produtos[produto] = preco
   n += 1  

total = sum(produtos.values())
print(f'\nO total da sua compra ficou em: R$ {total:.2f}')

#AQUI ESTAMOS UTILIZANDO O DICIONARIO PARA ARMAZENAR OS PRODUTOS E SEUS VALORES.
#REALIZANDO A OPERAÇÃO DE SOMA DE VALORES INT E PRINTANDO AO FINAL.
# :.2F COLOCA AUTOMATICAMENTE 2 CASAS DECIMAIS EM FLOAT.