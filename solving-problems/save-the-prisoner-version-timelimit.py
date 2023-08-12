def saveThePrisoner(n, m, s):
    prisioner = s
    first = 0
    while m > 0: # while have candies
        print(f"INIT candies: {m} -- prisioner: {prisioner} -- first: {first}")
        if m == 1:
            return prisioner

        if prisioner == n: 
            print("end")
            prisioner = 1          
        else:
            print("not first")
            prisioner +=1
        
        m -= 1
        first = 1
        print(f"END candies: {m} -- prisioner: {prisioner} -- first: {first}")

n = 5 
m = 2 
s = 1
saveThePrisoner(n,m,s)