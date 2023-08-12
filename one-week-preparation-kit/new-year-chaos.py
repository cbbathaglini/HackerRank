def minimumBribes(q):
    #print(f"q: {q}")
    arr_final = []
    arr_aux = []
    sort_array = q.copy()
    sort_array.sort()
        
    print(f"q: {q}")
    print(f"s: {sort_array}")
    count = 0
    for i in range(len(q)):
        for j in range(i,len(sort_array)):
            if q[i] > sort_array[j]:
                arr_final.append(q[i])
                print(f"{q[i]} ultrapassou o {sort_array[j]}")
    
    num_most_common = most_common(arr_final)
    
    if  arr_final.count(num_most_common)>= 3:
        print("Too chaotic")
    else:
        print(f"{len(arr_final)}")