print('Generation Finder')
name = (input('Enter Name Below: \n')).title()
year = int(input('Enter year of birth below: (e.g: 2009) \n'))
#checks the year falls into appropriate range, then sets generation to equal the corrosponding year.
if year < 1901 or year > 2023:
    print('Error! Please enter a valid year of birth which does not predate 1901 or surpass 2023')
else:
    if year >= 1901 and year <= 1924:
        generation = 'Greatest Generation'
    elif year > 1924 and year < 1946:
        generation = 'Silent Generation'
    elif year > 1945 and year < 1981:
        generation = 'Baby Boomers'
    elif year > 1980 and year < 1997:
        generation = 'Generation X'
    elif year > 1996 and year < 2013:
        generation = 'Generation Z'
    elif year > 2012:
        generation = 'Generation Alpha'
    print(f'Hello {name}, your generation is {generation}.')
