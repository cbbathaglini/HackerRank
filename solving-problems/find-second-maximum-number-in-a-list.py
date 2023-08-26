if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    list_arr = list(arr)
    
    list_arr.sort(reverse=True)
    
    first_number = 0
    for i in range(n):
        if i ==0:
            first_number = list_arr[i]
        if list_arr[i] != first_number:
            print(f"{list_arr[i]}")
            break