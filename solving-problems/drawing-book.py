
#https://www.hackerrank.com/challenges/drawing-book/problem

def pageCount(n, p):
    turns_first_last = 0
    turns_last_first = 0
        
    pages_count = 2
    arr_pages = []
    arr_pages.append([1])
    while pages_count < n:
        arr_pages.append([pages_count,pages_count+1])
        pages_count += 2
    
    if(n%2==0):
        arr_pages.append([n])
    
    #print(f"{arr_pages}")
    for i in range(len(arr_pages)):
        if p in arr_pages[i]:
            turns_first_last = i
            print(f"first-last: turn {i}x")
            #break
              
    arr_pages.reverse()
    #print(f"{arr_pages}")
    for i in range(len(arr_pages)):
        if p in arr_pages[i]:
            turns_last_first = i
            #print(f"last-first: turn {i}x")
            break
    
    if turns_last_first <= turns_first_last:
        return turns_last_first
    return turns_first_last

n = 5
p = 5
result = pageCount(n, p)