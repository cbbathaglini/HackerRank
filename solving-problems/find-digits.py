def findDigits(n):
    divisor =0
    split_str = str(n)
    for i in range(len(split_str)):
        if int(split_str[i]) !=0:
            if n% int(split_str[i])==0:
                divisor +=1
    return divisor