num = 75869
count = 0

while num > 0:
    num = num // 10
    count += 1
    
print('digitos:', count)

'''Em Python, o operador // é utilizado para realizar uma divisão inteira entre dois números. O resultado da operação é o quociente da divisão, desconsiderando qualquer parte fracionária que possa existir.

Por exemplo, se quisermos calcular a divisão inteira de 7 por 2, podemos usar o operador // da seguinte forma:'''

'''>>> 7 // 2
3
'''

'''Nesse caso, o resultado é 3, pois 2 cabe três vezes em 7, e sobra 1 de resto.

É importante notar que o operador / em Python realiza uma divisão comum, que inclui a parte fracionária. Se quisermos obter apenas a parte inteira do resultado da divisão, podemos usar o operador //.'''