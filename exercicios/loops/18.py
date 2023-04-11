# p=1
# final = 6
# start = 0
# aux = 0
# for i in range(start,final,p):
#     for j in range(i):
#         print('*', end=' ')
    
#     print('\n')
#     if i == 4:
#         final = 0
#         start = 5
#         p = -1
        
        
        
rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")
