print('Tip calculator')
amount_to_pay = float(input('How much do you have to pay ?\n'))
people_paying = int(input('How many persons split the bill ?\n'))
tip_percent = int(input('Tip percent from the bill\n'))


def calculate_tip(pay, tip_perc, people):
    tip = (pay * tip_perc / 100) / people
    return round(tip, 2)

tip = calculate_tip(amount_to_pay, tip_percent, people_paying)
total_amount = tip + amount_to_pay / people_paying
print("Tip you shoud pay per person\n" + str(calculate_tip(amount_to_pay, tip_percent, people_paying)))

print(f'Total per person: {round(total_amount, 2)}' )