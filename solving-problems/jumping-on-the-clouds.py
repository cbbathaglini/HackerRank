def jumpingOnClouds(c):
    jumps = 0
    i =0
    while i< len(c)-1:
        if c[i] == 0:         
            if i+2 < len(c) and c[i+2] == 0:
                jumps+=1
                i+=2
            elif c[i+1] == 0 and i+1 < len(c):
                jumps+=1
                i+=1
            elif c[i+1] == 1:
                jumps+=1
                i+=2
        elif i ==0 and c[i] == 1:
            jumps +=1
    return jumps