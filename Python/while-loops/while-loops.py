i = 1

# while(i<10):
#     print('em loop')
loop = True
while (loop):
    print(i)
    i+=1
    
    if i>10:
        loop = False
        
tecla = ' '
while (tecla!='q'):
   tecla = input('aperte uma tecla')
   
#o Break pula direto pro final do while e encerra o loop
#o continue volta pro começo do while a partir de onde ele está

# pedro,sp=1500
# aline,sp=1500
# rafael,sp=1500
# rafaela,rn=5000
# alisson,ce=5000

# while (True):
#     if estado != 'sp':
#         continue

#EXEMPLO DE COMO PEGAR INFORMAÇÕES ESPECIFICAS USANDO O CONTINUE, JÁ QUE SEMPRE VOLTARIA PARA O COMEÇO USANDO ELE SEMPRE QUE NÃO FOR A INFORMAÇÃO Q EU QUERO