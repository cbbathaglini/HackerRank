# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
NM = input()
N = NM.split()[0]
M = NM.split()[1]


array = []
for i in range(int(N)):
    line = input()
    arrpositions = []
    position = line.split()
    for j in range(int(M)):
        arrpositions.append(int(position[j]))
    array.append(arrpositions)
    
minarr = numpy.min(array, axis = 1)
print(numpy.max(minarr)) 
