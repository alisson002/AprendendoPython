num = list(input('Digite um numero para verificarmos se ele é palidromo: '))

x = num.copy()
x.reverse()
#se não fizer dessa forma a lista não é inverida correctamente
#se o reverse for aplicado diretamente em num, vai alterar a lista original e para a comparação ainda precisarei dela

if num == x:
    print('numero palidromo')
else:
    print('não e numero palidromo')
    
#como função
# num = int(input('Digite um numero para verificarmos se ele é palidromo: '))

# def palidromo(num):
    
#     num = list(num)
    
#     x = num.copy()
#     x.reverse()
    
#     if num == x:
#         print('numero palidromo')
#     else:
#         print('não e numero palidromo')