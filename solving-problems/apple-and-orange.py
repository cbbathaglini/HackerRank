#https://www.hackerrank.com/challenges/apple-and-orange/submissions/code/339197382
def countApplesAndOranges(s, t, a, b, apples, oranges):
    
    #print(f"apples:{apples}")
    soma_macas = 0
    soma_laranjas = 0
    for i in range(len(apples)):
        #print(f"a + apples[i]:{a + apples[i]}")
        if (a + apples[i]) >= s and (a + apples[i]) <= t: 
            soma_macas +=1
    
    #print(f"apples:{oranges}")
    for i in range(len(oranges)):
        #print(f"a + oranges[i]:{b + oranges[i]}")
        if (b + oranges[i]) >= s and (b + oranges[i]) <= t: 
            soma_laranjas+=1
        
    print(f"{soma_macas}")
    print(f"{soma_laranjas}")