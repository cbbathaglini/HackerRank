def getMoneySpent(keyboards, drives, b):

    arr_possibilities = []

    for i in range(len(keyboards)):
        for j in range(len(drives)):
            if keyboards[i] + drives[j] <= b:
                #arr_possibilities.append({"key":keyboards[i], "drive":drives[j],"total_price": keyboards[i] + drives[j]})
                arr_possibilities.append( keyboards[i] + drives[j])
    
    arr_possibilities.sort(reverse=True)
    if len(arr_possibilities) == 0:
        arr_possibilities.append(-1)
        
    return arr_possibilities[0]