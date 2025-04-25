#Atividades 5 - Façam uma função que receba dois números e retorne a todas os cálculo acima entre eles 

def matfull(num1,num2):
    soma = num1 + num2
    div = num1 / num2
    mult = num1 * num2
    sub = num1 - num2
    print('-='*30)
    return f'Vamos calcular todas as operações!\n Soma = {soma}.\n Divisão = {div}.\n Multiplicação = {mult}.\n Subtração = {sub}.'

adicionar1 = int(input('Numero 1: '))
adicionar2 = int(input('Numero 2: '))

print(matfull(adicionar1,adicionar2))
