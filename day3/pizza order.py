bill = 0

order = input('order size: ')
extra = input('extra: ')


if order == 'L':
    bill = 25
elif order == 'M':
    bill = 20
elif order == 'S':
    bill = 15
if extra == 'Y' and order == 'S':
    bill += 2
    print(bill)
elif extra == 'Y' and order == 'L' or order == 'M':
    bill += 3
    print(bill)
if extra == 'N':
    bill += 1
    print(bill)
