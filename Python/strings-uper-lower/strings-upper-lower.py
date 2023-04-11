string1 = 'alisson moreira'
string2 = 'manipulando strings em python'

print(string1 + string2)#concatena uma string coma outra
print(string1,string2)#imprime as duas separando por espaço, um em seguida da outra
print(string1 +' '+ string2)#concaneção com espaço

print(len(string1))#tamanho da string

string3 = string1 + string2
print(string3)


string4 = string1.replace('alisson','moreira')#troca a primeira palavra pela segunda
#não muda a string 1
print(string4)

print(string1.find('moreira'))#retornar um numero: qual a possição de 'moreira' em 'alisson moreira' = 9
print(string1.find('alisson'))#0
print(string1.find('sson'))#3
#quando não existe na string ele retorna -1

if string1.find('joao') == -1:
    print('não existe na string')
else:
    print('existe na string')
    
print(string2.split())#divide a string em tokens, separa como se fosse uma lista de string ['manipulando', 'strings', 'em', 'python']

lista = string2.split()#para imprimir uma palavra de cada vez da lista gerada com o .split
for i in lista:
    print(i)
    
for i in lista:
    
    if i == 'em':
        i = ''
    
    print(i)
    
for i in lista:
    
    if i == 'em':
        #i = ''
        continue#com o continue ele tira o espaço da substituição
    
    print(i)
    
string1.upper()#todas em maiusculo
string1.lower()#todas em minusculo
string1.lower().capitalize()#a primera letra da string em maiusculo e o resto em minusculo
string1.lower().title()#deixa em maiusculo as primeiras de cada palavra
string1.lower().title().swapcase()#inverte maiusculo com meniusculo

#funções para checagem
if string2.isupper():#para saber se está em uppercase
    print('MAIUSCULO')#imprime se for true
    
string2.islower()
string2.istitle()
string2.isnumeric()
string2.isalpha()
string2.isspace()
string2.isdigit()


print(string1.strip())#removeos espaços em branco ' alisson moreira ' sai sem o espaço do começo e do final

# string1.rstrip()#tira os espaçoes a direita
# string1.lstrip()#tira os espaçoes a esquerda
#string1.ljust(40)#justifica a esquerda com 40 caracteres
#string1.center(40)#alinha ao centro com 40 caracteres

print('string tb podem set utilizadas assim: %s, %s, %s' %(string1, string2, string3))#vão aparecer na ordem do parenteses



'''%s refers to a string data type, %f refers to a float data type, and %d refers to a double data type.'''
'''%o converte o numero para tipo para octal'''



