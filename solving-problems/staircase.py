#https://www.hackerrank.com/challenges/staircase/submissions/code/339026148
def staircase(n):
    for i in range(n):
        for j in range(n):
            if (j == n-1) or (i == n-1):
                print("#", end="")
            elif(j>= (n-1-i)):
                print("#", end="")
            else:                  
                print(" ", end="")
        print("",end="\n")
