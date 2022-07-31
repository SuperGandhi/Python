# ámbito global 
today_weither = 12.0;

def my_func(name):
    # ámbito de la función
    today_weither = 10.0;
    print('Hi ', name, 'temperature of the: ' , today_weither)

my_func('Pat')
# variable shadowing
print(today_weither)

# cuando tenemos mucho parametros podemos usar la sgte convención
def sum(*args):
    result = 0
    for arg in args:
        result += arg
    print(result)
    
sum (1,3,4,543,53,412,12,343,14465,42323)

# para parametros con nombres(names parameters)
# def names(**kwargs):
#     if kwargs['lastname'] == 'Borja':
#         return 
    
#     for key, value in kwargs.items():
#         print(key, '-', value)

# names(lastname='Borja', book='La República')

def sum (**kwargs):
    initial = kwargs['initial'] if 'initial' in kwargs else 0
    # operador ternario 
    final = kwargs['final'] if 'final' in kwargs else 0
    
    result = 0
    for x in range (initial, final + 1):
        result += x
        return result

print(sum(final=15))

#funciones anónimas o lambda
anonymous = lambda name,name2: print('hi', name, 'bye', name2)
anonymous('ross', 'jul')


sumatoria = lambda x: x + x
print(sumatoria(2))