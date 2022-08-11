secret = 50

value =  0
while value != secret:
    value = int(input('Entry your number: '))
    
    if value > secret:
        print('SO HIGH')
        continue
    
    if value < secret:
        print('SO LOW')
        continue
    
print('YOU WIN')
