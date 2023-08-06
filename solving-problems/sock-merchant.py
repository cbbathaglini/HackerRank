#https://www.hackerrank.com/challenges/sock-merchant/submissions/code/339496841
def sockMerchant(n, ar):
    pairs = 0
    for i in range(len(ar)):
        for j in range(len(ar)):
            if(ar[i] == ar[j] and i != j and ar[i] != 'X' and ar[j] !='X'):
                pairs += 1
                ar[i] = 'X'
                ar[j] = 'X'   

    return pairs