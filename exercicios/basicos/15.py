print('a seguir defina a potência')
print('\n')

base = int(input('base da potencia: '))
# if type(base) != "<class 'int'>":
#     base = int(input('base da potencia: '))

expoente = int(input('expoente da potencia: '))
if expoente < 0:
    expoente = int(input('expoente da potencia: '))
    
def pot(base, expoente):
    resultado = base**expoente
    print(base,'elevado a',expoente,'eh igual a: ',resultado)

pot(base,expoente)