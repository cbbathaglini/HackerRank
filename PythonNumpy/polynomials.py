import numpy

coeficientes = input()
x_value = float(input())

coeficientes_split = coeficientes.split()
array_coeficientes = []
for i in range(len(coeficientes_split)):
    array_coeficientes.append(float(coeficientes_split[i]))

#print(array_coeficientes)
#x_value^coeficiente[0] + x_value^coeficiente[1] + x_value^coeficiente[2] 
print(numpy.polyval(array_coeficientes, x_value))
