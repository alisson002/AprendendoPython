# import random
# from random import choices, sample

# #

# tamanho = 12
# valores = range(1, 51)#retorna *range(1, 51)* que é do tipo <class 'range'>

# print(choices(float(valores), k=tamanho))
# print(sample(float(valores), tamanho))

from random import uniform

tam_list = int(input('digite o tamanho da lista: '))

num_list = []

for i in range(tam_list):
    num_list.append(float(input('Digite um float: ')))
    
print(num_list)

'''OUTRA FOTMA DE FAZER'''
tamanho = 12
valores = [round(uniform(0, 1000),4) for _ in range(20)]#retorna *range(1, 51)* que é do tipo <class 'range'>

print(valores)