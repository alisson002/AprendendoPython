str = str(input('digite uma palavra ou frase: '))

xstr = list(str.replace(" ", ""))

print(xstr)

def remove(string, num):
    for i in range(num):
        string.pop(0)
    
    return string
        
remove(xstr, 4)

xstr = ''.join(xstr)

print(xstr)
