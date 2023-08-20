def findZigZagSequence(a, n):
    a.sort()
    mid = int((n + 1)/2) 
    a[mid], a[n-1] = a[n-1], a[mid]
    print(f"{a}")

    st = mid + 1
    ed = n - 1
   
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        print(f"-- {a}")
        st = st + 1
        ed = ed + 1
        print(f"st: {st} | ed: {ed}")

    for i in range (n):
        if i == n-1:
            print(f"{a[i]}")
        else:
            print(f"{a[i]}", end = ' ')
    return

#   [1 2 3 4 5]   ==>   [1 4 5 3 2]
#        ^
# [1 2 3 4 5 6 7] ==> [1 2 3 7 6 5 4]
#        ^  
#  1 2 3 4 5 6 7
#  1 2 3 7 5 6 4
#  
#  
#[1,2,3,4,5]
#[1,2,5,4,3]

n = 7
a = [1, 2, 3, 7, 6, 5, 4] # [1 2 3 7 6 5 4]


# [1 2 3 4 5 6 7]
# [1 2 3 7 5 6 4]
# [1 2 3 7 6 5 4]


n = 5
a = [2,3,5,1,4]
# ultimo com segundo
# ordena
#[1,2,3,4,5]
# 0 1 2 3 4
# trocar as posicoes do meio do array (posicao: 3) para ultima posicao
# [1 2 3 5 4]
# st => posicao 4 e ed: 4
# [1 2 3 5 4]
#          ^         
# [1 2 3 4 5 6]
# [1 ]
findZigZagSequence(a,n)


#[1,4,5,3,2]