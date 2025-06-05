usuario = {}

print()
print('PREENCHA TODAS AS INFORMAÇÕES A BAIXO:')
print()
usuario['Nome'] = input('Nome: ')
usuario['Telefone'] = input('Telefone: ')
usuario['Email'] = input('Email: ')

print(f'=-=-'*21)
for chave, valor in usuario.items():
    print(f'Seu {chave} está como "{valor}"')
print(f'=-=-'*21)

