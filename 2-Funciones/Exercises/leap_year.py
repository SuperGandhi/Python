

leap_year = lambda year: print('Is leap' if not year % 4 and(year % 100 or not year % 400)else'Not is leap')
leap_year(2022)