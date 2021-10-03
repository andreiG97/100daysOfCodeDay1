height = int(input('Enter height: '))

if int(height) > 120:
    print('Go')
else:
    print('Stay')

if height % 2 == 0:
    print('Height is even')
else:
    print('Height is odd')
