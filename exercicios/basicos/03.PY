str = str(input('digite uma palavra ou frase: '))

xstr = list(str.replace(" ", ""))

print(xstr)

for i in range(0,len(xstr),2):
    print(xstr[i])
    
for i in xstr[0::2]: 
    print(i)