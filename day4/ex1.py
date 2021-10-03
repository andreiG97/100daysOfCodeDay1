import random

# heads = 'heads'.capitalize()
# tails = 'tails'.capitalize()
#
# my_list = [heads, tails]
# i = random.randint(0,1)
# print(my_list[i])

# employees = input('Enter names:')
# list_emp = employees.split(',')
#
# i = random.randint(0, list_emp.__len__()-1)
# print(list_emp)
# print(list_emp[i])

row1 = ['#', '#', '#']
row2 = ['#', '#', '#']
row3 = ['#', '#', '#']

treasure_map = [row1, row2, row3]

print(f'{row1}\n{row2}\n{row3}')
x = int(input('Mark the x: '))
y = int(input('Mark the y: '))

treasure_map[x][y] = 'X'
print(f'{row1}\n{row2}\n{row3}')
