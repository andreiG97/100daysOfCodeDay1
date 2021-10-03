year = int(input('Year: '))


def weeks(year):
    weeks_per_year = 365 // 7
    years_left = 2090 - year
    weeks_left = weeks_per_year * years_left
    months_left = weeks_left // 4
    return weeks_left, months_left


print(weeks(year))
