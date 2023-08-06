#https://www.hackerrank.com/challenges/np-sum-and-prod/submissions/code/338475976

# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy


NM = input()
N = NM.split()[0]
M = NM.split()[1]

#print(f"N: {N}")
#print(f"M: {M}")

array = []
for i in range(int(N)):
    line = input()
    arrPositions = []
    position = line.split()
    for j in range(int(M)):
        arrPositions.append(int(position[j]))
    array.append(arrPositions)    
    #print(array)

#my_array = numpy.array([ [1, 1, 1], [1, 1, 1] ])
#axiszero = numpy.prod(my_array, axis = 0)
#print(f"my_array: {my_array}")
#print(f"axiszero: {axiszero}")
#print(numpy.prod(axiszero))
axiszero = numpy.sum(array, axis = 0)
#print(axiszero)
print(numpy.prod(axiszero))
