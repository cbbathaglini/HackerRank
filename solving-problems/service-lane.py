def serviceLane(n, cases,width):
    arr_return = []
    for i in range(len(cases)):
        position = cases[i]
        arr_return.append(min(width[position[0]:position[1]+1]))
    return arr_return