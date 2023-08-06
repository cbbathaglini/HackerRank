import numpy
A = input()
B = input()

Asplit = A.split()
Bsplit = B.split()

arrayA = [] 
for i in range(len(Asplit)):
    arrayA.append(int(Asplit[i]))
    
arrayB = []
for i in range(len(Bsplit)):
    arrayB.append(int(Bsplit[i]))

#print(arrayA)
#print(arrayB)
print(numpy.inner(arrayA, arrayB))
print(numpy.outer(arrayA, arrayB))
