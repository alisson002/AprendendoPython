num = int(input('Range da soma: '))

print('Printing current and previous number sum in a range(', num,')')

Current = 0
Previous = 0
Sum = 0

for i in range(num):
    print('Current Number:', i, 'Previous Number:',  Previous,  'Sum:',  Sum)
    Previous = Current
    Current = Current+1
    Sum = Previous + Current
    
# print("Printing current and previous number and their sum in a range(10)")
# previous_num = 0

# # loop from 1 to 10
# for i in range(1, 11):
#     x_sum = previous_num + i
#     print("Current Number", i, "Previous Number ", previous_num, " Sum: ", x_sum)
#     # modify previous number
#     # set it to the current number
#     previous_num = i