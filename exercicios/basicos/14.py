tam = int(input('Tamanho da piramide: '))

for j in range(tam+1,0,-1):#iteração decrescente
    for i in range(0, j-1):
        print('*', end=' ')
        
    print('\t')
    