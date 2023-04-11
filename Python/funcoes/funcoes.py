def minha_funcao():
    print('minha função')
    
minha_funcao()

def minha_funcao2(parametro):
    print('parametro: '+parametro)
    
    print('parametro: '+parametro.replace(' ','-'))
    
    parametro = parametro.replace(' ','-')
    parametro = 'https://www.google.com/' + parametro
    
    print('minha função, parametro: ' + parametro)
    
minha_funcao2('curso de python')

def criar_diretorio(*args):#para quando não se sabe o tanto de argumento que serão recebidos
    #usa dois* se não souber oq eu vai receber de variavel
    print(args[0])# so imprime o primeiro argumento
    print(args)#imprime todos
    
criar_diretorio('curso de python','alisson moreira','programação')

def calculo(n):
    return n*3
print(calculo(2))

def calculo2(n):
    return n**3#potencia
print(calculo2(2))

#  PARA IMPORTAR MODULOS USA:
# from <modulo aqui> import * -> dessa forma so vai precisar chamar diretamente oq vc precisa
# import <modulo aqui> -> assim vai precisar usar modulo.<função>