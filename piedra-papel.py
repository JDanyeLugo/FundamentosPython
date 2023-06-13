#Elección aleatoria Maq
import random

# function randint (random.randint (1,3))
rand_int = random.randint (1,3)
if rand_int == 1:
    choice_maq = 'piedra'
elif rand_int == 2:
    choice_maq = 'papel'
else:
    choice_maq ='tijeras'

#Elección de usuario
choice_text = '''
Escribe una de las opciones:
    piedra
    papel
    tijeras
'''
choice_user = input(choice_text)

#Impresión de opcciones
print('usuario eligio ->', choice_user)
print('Maquina eligio ->', choice_maq)
#Ganado!

if choice_maq == choice_user:
    print("Es un empate")
else:
    if choice_maq == 'piedra'and choice_user == 'papel':
        print('Gana usuario')
    elif choice_maq == 'piedra' and choice_user == 'tijeras':
        print('Gana maquina')
    elif choice_maq == 'papel' and choice_user == 'tijeras':
        print('Gana usuario')
    elif choice_maq == 'papel' and choice_user == 'piedra':
        print('Gana Maquina')
    elif choice_maq == 'tijeras' and choice_user == 'piedra':
        print('Gana maquina')
    else:
        print('Gana usuario')