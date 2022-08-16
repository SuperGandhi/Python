weight = input("Ingrese su peso: ")
height = input("Ingrese su estatura: ")
imc = round(float(weight) / float(height)**2,2)
print('Tu IMC es ' + str(imc))