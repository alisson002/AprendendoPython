almoço = ['macarrão','feijão','farofa','carne','arroz','frango']
comida = 'arroz'

if comida in almoço:
    print('esta na lista')

comida = 'pera'
if comida not in almoço:
    print('não está na lista')
    
#nos dicionarios os elementos são referenciados por uma key-value
clientes = {'nome':'Pedro','idade':'46'}
print(clientes)

clientes['cep'] = '62840000'
print(clientes)

clientes['nome'] = clientes['nome'].upper()
print(clientes)

cliente = {}#tb é possivel criar assim
cliente['nome'] = 'Pedro'
cliente['idade'] = '46'
cliente['cep'] = '62840000'
print(cliente)

del cliente['cep']#para deletar uma key-value
print(cliente)

print(type(cliente))

print(clientes.items())

print(clientes.keys())

print(clientes.values())

for key,value in clientes.items():
    print(key,value)#imprime cada key-value uma abaixo da outra
    
for key,value in clientes.items():
    print(value, key)#imprime invertido
    
clientes['dados'] = {'casa': 'prorpia', 'carro': 'ford'}
print(clientes)

clientes = {'nome':'Pedro','idade':'46','cep':'62840000','dados' : {'casa': 'prorpia', 'carro': 'ford'}}
clientes = {
    'nome':'Pedro',
    'idade':'46',
    'cep':'62840000',
    'dados' : {
        'casa': 'prorpia', 
        'carro': 'ford'
    }
}

for key,value in clientes.items():
    print(key,value)
    
    if isinstance(value, (dict)):
        print('dicionario encontrado')#para saber se o valor encontrado é do tipo dict
        
# for key,value in clientes.items():
#     print(key,value, type(value))
    
#     if type(value) == '<class dict>':
#         print()