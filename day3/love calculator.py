first_name = input('First person name')
second_name = input('Second person name')

first_count = 0
second_count = 0

first_name = first_name.lower()
second_name = second_name.lower()

expression1 = 'TRUE'
expression2 = 'love'
expression = expression1.lower()

for i in expression:
    first_count += first_name.count(i)
    first_count += second_name.count(i)
for i in expression2:
    second_count += first_name.count(i)
    second_count += second_name.count(i)

print(str(first_count) + str(second_count))
