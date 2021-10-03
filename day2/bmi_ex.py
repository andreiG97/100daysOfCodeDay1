weight = int(input('Enter weight: '))
height = float(input('Enter height: '))


def calculate_body_mass_index(w, h):
    index = w / (h**2)
    return int(index)


print(calculate_body_mass_index(weight, height))

