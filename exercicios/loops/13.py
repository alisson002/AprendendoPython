num = int(input('defina um numero: '))
fac = 1
for i in range(num, 0, -1):
    fac *= i
    
print(fac)

fac2 = 1
for i in range(1,num+1):
    fac2 *= i
    
print(fac2)