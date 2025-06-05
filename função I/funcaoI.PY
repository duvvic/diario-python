#[PYIA-A04]

def media(numero1,numero2,numero3):
    soma = (numero1 + numero2 + numero3) / 3
    print(f'Sua media é: {soma}')
    
n1 = float(input('digite o primeiro numero: '))
n2 = float(input('digite o segundo numero: '))
n3 = float(input('digite o terceiro numero: '))

media(n1,n2,n3)