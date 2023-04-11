linhas = int(input('Quantas linhas?: '))

for i in range(linhas+1):
    for j in range(i):
        print(i, end=' ')
    
    print('\n')