# lista1 = []
# tam1 = int(input('tamanho da lista1: '))

# while len(lista1) < tam1:
#     addElement = int(input('Digite um numero inteiro para ser adicionado na lista 1: '))
#     lista1.append(addElement)
    
# lista2 = []
# tam2 = int(input('tamanho da lista1: '))

# while len(lista2) < tam2:
#     addElement = int(input('Digite um numero inteiro para ser adicionado na lista 2: '))
#     lista2.append(addElement)

import random
from random import choices, sample

lista1 = []
tam1 = random.randint(5, 15)

lista2 = []
tam2 = random.randint(5, 15)

lista3 = []

for i in range(tam1):
    lista1.append(random.randint(0, 100))
    if lista1[i]%2 != 0:
        lista3.append(lista1[i])
    
for i in range(tam2):
    lista2.append(random.randint(0, 100))
    if lista2[i]%2 == 0:
        lista3.append(lista2[i])
        
print(lista1)
print(lista2)
print(lista3)

print('\n')
print('outras formas de criar listas -automaticas- sem precisar de loops')

tamanho = 12
valores = range(1, 51)#retorna *range(1, 51)* que é do tipo <class 'range'>

print(choices(valores, k=tamanho))
print(sample(valores, tamanho))

# The sample() method returns a list with a randomly selection of a specified number of items from a sequnce.
# Note: This method does not change the original sequence.
# random.sample(sequence, k)
# Parameter	Description
# sequence	Required. A sequence. Can be any sequence: list, set, range etc.
# k	        Required. The size of the returned list


# The choices() method returns a list with the randomly selected element from the specified sequence.
# You can weigh the possibility of each result with the weights parameter or the cum_weights parameter.
# The sequence can be a string, a range, a list, a tuple or any other kind of sequence.
# random.choices(sequence, weights=None, cum_weights=None, k=1)
# Parameter	Description
# sequence	Required. A sequence like a list, a tuple, a range of numbers etc.
# weights	    Optional. A list were you can weigh the possibility for each value.
#             Default None
# cum_weights	Optional. A list were you can weigh the possibility for each value, only this time the possibility is accumulated.
#             Example: normal weights list: [2, 1, 1] is the same as this cum_weights list; [2, 3, 4].
#             Default None
# k	        Optional. An integer defining the length of the returned list

# def merge_list(list1, list2):
#     result_list = []
    
#     # iterate first list
#     for num in list1:
#         # check if current number is odd
#         if num % 2 != 0:
#             # add odd number to result list
#             result_list.append(num)
    
#     # iterate second list
#     for num in list2:
#         # check if current number is even
#         if num % 2 == 0:
#             # add even number to result list
#             result_list.append(num)
#     return result_list

# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]
# print("result list:", merge_list(list1, list2))
