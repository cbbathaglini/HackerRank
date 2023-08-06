#https://www.hackerrank.com/challenges/kangaroo/submissions/code/339199599
def kangaroo(x1, v1, x2, v2):
    
    if (x2 > x1) and ( v2 > v1): 
        return "NO"
    
    #print(f"{abs(x2 - x1)} || {abs(v2 - v1)}") 
    diff_x = abs(x2-x1)
    diff_v = abs(v2-v1)
    if diff_v >0:
        calculo  = abs(x2 - x1) % abs(v2-v1)
        #print(f"{calculo}") 
        if ( calculo == 0 ) :
            return "YES"
    return "NO"