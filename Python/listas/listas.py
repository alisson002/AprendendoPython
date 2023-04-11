frutas = ['maçã', 'banana', 'pera', 'uva']
print(frutas)#imprime a lista toda

print(frutas[0])#primeiro elemento
print(frutas[1])#segundo elemento
print(frutas[-1])#ultimo elemento
print(frutas[-2])#penultimo elemento

frutas[2] = 'melancia'#troca o elemento
print(frutas)

del frutas[2]#remove o elemento e reorganiza a lista
print(frutas)

frutas.sort()#organiza por ordem alfabetica no caso de strings
print(frutas)

frutas = ['maçã', 'banana', 'pera', 'uva', 'amora', 'melão']
frutas.sort()#organiza em ordem alfabetica
frutas.reverse()#inverte a ordem da lista
print(frutas)

frutas = ['maçã', 'banana', 'pera', 'uva', 'amora', 'melão']
frutas.reverse()#inverte a ordem da lista
print(frutas)

print(len(frutas))#retorna quantos elementos tem na lista

frutas = ['maçã', 'banana', 'pera', 'uva', 'amora', 'melão']
for i in frutas:
    print(i)#lista todos os elementos da lista
    
for i in frutas:
    if i == 'uva':
        print('elemento encontrado')
    
    print(i)
    
print(frutas[1:4])#imprime os elementos de 1 a 3

frutas2 = frutas.copy()#para que não tenha alterações na original


frutas3 = ['maçã', 'banana', 'pera', 'uva', 'amora', 'melão']
print(frutas3)
frutas3.insert(1, 'carro')#insere um elemento na lista sem eliminar os outro, somente alterando as posições
print(frutas3)
frutas3.extend('fusca')#coloca o elemento separado por letra dentro da lista
print(frutas3)

frutas3.append('moto')#adiciona sempre ao final da lista
print(frutas3)

frutas3.remove('carro')#remove elemento especifico
print(frutas3)

frutas3.sort()#orgaiza em ordem alfabetica
print(frutas3)

frutas3.sort(reverse=True)
print(frutas3)

print(sorted(frutas3))#função para ordem alfabetica que não altera a lista de forma permanente)

frutas3.reverse()#coloca a lista em ordem reversa

numeros = list(range(1,100))#lista de 1 a 99

frutas3[2:4]#pega do elemento 2 ao 4-1. se não colocar nada vai ate o final.
frutas3[::2]#pega de 2 em 2 ate o final
frutas3[-3:]#pega os 3 ultimos #pega de 2 em 2 ate o final

frutasCopy = frutas3[:]
frutasCopy = frutas3.copy()

print(list(range(4, 30, 2)))#para gerar listas

x = [4, 6, 8, 24, 12, 2]
print(max(x))#maior numero de uma lista

