class Band:
    def __init__(self, city_name, special_name):
        self.city_name = city_name
        self.special_name = special_name
        self.band_name = city_name + special_name.capitalize()

    def generate_name(self):
        return self.band_name


first_name = input('City where you were born: ')
second_name = input("Animal or hobby that you had in your childhood: ")

band1 = Band(first_name, second_name)
print(band1.generate_name())
