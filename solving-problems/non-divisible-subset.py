#### NOT COMPLETE

def nonDivisibleSubset(k, s):
    possibilities = []
    possibilities_aux = []
    
   
    for i in range(len(s)):
        soma_ok = True
        j = 1
        soma = s[i]
        possibilities = []
        while soma_ok:
            soma  += s[j]
            print(f"-soma->{soma} = {soma % k}")
            
            if soma % k != 0 :
                if s[i] not in possibilities: possibilities.append(s[i])
                if s[j] not in possibilities: possibilities.append(s[j])

            j+=1
            print(f"j: {j}")
            if j == len(s):
                print(f"-->here")
                possibilities.sort()
                print(f"possibilities: {possibilities} => {sum(possibilities)}%{k}={sum(possibilities)%k}") 
                nonDivisibleSubset(k,possibilities)
                break
 
    return len(s)         


k = 4
a = [19,10,12,10,24,25,22]
nonDivisibleSubset(k,a)