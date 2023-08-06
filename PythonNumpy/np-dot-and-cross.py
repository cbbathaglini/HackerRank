#https://www.hackerrank.com/challenges/np-dot-and-cross/submissions/code/338480522
import numpy
N = int(input())

arrayAB = []
arraux = []
for i in range(int(N*2)):
    line = input()
    arrpositions = []                
    position = line.split()
    for j in range(N):
        arrpositions.append(int(position[j]))
        
    arraux.append(arrpositions)
    #print(f"pos: {arrpositions} e N: {i}, aux: {arraux}")
    if( (i+1) % N == 0):
        arrayAB.append(arraux)
        arraux = []
    
#print(arrayAB)

print(numpy.dot(arrayAB[0] , arrayAB[1]))
