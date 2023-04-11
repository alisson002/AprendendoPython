#tupla é uma tabela, é uma sequencia de objetos imutaveis, diferente das listas
notebooks = ('hp','dell','compaq')
numeros = 2000,2500,1500,3000
processadores = 'intel','amd'
print(notebooks)
print(numeros)
print(processadores) 
print(numeros[0:2])

#notebooks[0] = 'apagado'#não aceita, pois não pode ter alteração

novo = notebooks + numeros#pode ser concatenado e armazenado e outra variável

print(novo)

for i in notebooks:#imprime um de cada vez
    print(i)
    