# O programa cria 2 numero aleatois de 1 a 6, e soma dois numeros.

import random
import faces_dados as fd

def lancar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    total = dado1 + dado2
    
    face1 = fd.desenhar_dado(dado1)
    face2 = fd.desenhar_dado(dado2)

    
    # Mostrar lado a lado
    for linha1, linha2 in zip(face1, face2):
        print(f"{linha1}   {linha2}")
    print(f"Soma: {total}\n")

# Rodar

while True:
    rodar = input('Bem vido ao game! Vamos jogar os dados\n [s] Para continuar\n [n] Fim do game\n Comando ->')
    if rodar == 's':
        lancar_dados()
    elif rodar == 'n':
        print('Boa sorte na proxima!')
        break
    else:
        print('Comando invalido')


