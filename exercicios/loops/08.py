list1 = [10, 20, 30, 40, 50]

for i in list1[::-1]:
    print(i)
    
# reverse list
new_list = reversed(list1)
# iterate reversed list
for item in new_list:
    print(item)