if __name__ == '__main__':
    arr = []    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.append([name,score])
            
    arr = sorted(arr, key=lambda x: x[1]) #ordena pelo numero
    
    arr_escolhidos = []   
    first_nota = arr[0][1]
    second = -1
    for i in range(len(arr)):
        if arr[i][1] != first_nota and second == -1:
            second = arr[i][1]
            arr_escolhidos.append(arr[i][0])
        elif arr[i][1] == second and second != -1:    
            arr_escolhidos.append(arr[i][0])
        
            
    nomes = sorted(arr_escolhidos, key=lambda x: x[0])
    print('\n'.join(nomes))