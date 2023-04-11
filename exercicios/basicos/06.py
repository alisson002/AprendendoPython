lista = []
tam = int(input('tamanho da lista: '))

while len(lista) < tam:
    addElement = int(input('Digite um numero inteiro para ser adicionado na lista: '))
    lista.append(addElement)
  
print('lista: ', lista)  
    
for i in range(tam):
    if lista[i]%5 == 0:
        print(lista[i])


