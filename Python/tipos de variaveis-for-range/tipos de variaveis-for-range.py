#POO: tudo é objeto. tudo que vc cria já é um objeto. para o python toda variavel é um objeto.

a = 10
b = 3.14
c = 'python'

print(type(a)) 
print(type(b))
print(type(c))
#quando eu rodo o programa, ele mostra que quando eu criei as variaveis ela ja foram criadas como objeto
#não precisa de ;
#maiusculo e minusculo tem diferença

#FOR: estrutura de looping
for i in range(5):
    print(i)#começa do 0 e vai até 5-1

for i in range(5):
    print(i+1)#começa do 1 e vai até 5


#estrutura condicional
x = 11
if x>10:
    print('x é maior a 10')
elif a==10:
    print('x é exatamente igual a 10')
else:
    print('x é menor a 10')

lista = ['janeiro', 'fevereiro', 'março']
for i in lista.copy():#por segunrança é melhor iterar em uma copia da lista
    print(i, len(i))#imprimindo os meses e o tamanho da palavra
    #print(i) imprimiria somente os meses. Vendo só o 'i' alí parece que vai imprimir as posições da lista, mas são os componentes delas mesmo.
    #for i in lista.copy():
        #print(i)

for i in range(5,10):
    print(i)#imprime de 5 a 10-1

for i in range(1,10):
    print(i)#imprime de 1 a 10-1

for i in range(0,10,2):
    print(i)#para contar de 2 em 2

for i in range(-10,10,2):
    print(i)#para contar de 2 em 2, tb trabalha com numeros negativos

for i in range(0,50):
    if i == 15:
        break

    print(i)#imprime ate parar no valor da condição

while True:
    pass#fica em loopin. e so pra se interromper a execução