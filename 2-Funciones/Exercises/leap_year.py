def leap_year(year):
    if(year % 4 == 0):
        pass
    if(year % 100 == 0):
        pass
    elif(year % 400 == 0):
        pass
    elif(year == 365):
        print('Yes is a leap year')
    else:
        print('Not is a leap year')

leap_year(1992)
        