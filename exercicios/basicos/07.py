# str_x = "Emma is good developer. Emma is a writer"

# insidencia = str_x.count('Emma')

# print('Emma parece', insidencia,'vezes na frase')

frase = str(input('Digite uma frase para vermos quantas vezes determinada palavra aparece nela: '))

palavra = str(input('Digite a palavra a ser procurada: '))

insidencia = frase.count(palavra)

print(palavra.title(), 'parece', insidencia,'vezes na frase')

#nesse caso vai procurar a exata palavra, levando em consideração maiusculo e menusculo


