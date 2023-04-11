num = int(input('digite um numero inteiro: '))
print(num)
print(type(num))

x = str(num)[::-1]
# x.reverse()
print(x)
print(type(x))

for _ in x:
    print(_, end=' ')

#tem outras formas de inverter
#pode ser tb transformando em uma lista para então ela ser invertida

# number = 7536
# print("Given number", number)
# while number > 0:
#     # get the last digit
#     digit = number % 10
#     # remove the last digit and repeat the loop
#     number = number // 10
#     print(digit, end=" ")