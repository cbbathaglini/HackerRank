#  _____________________
#  |100|100|___|___|___|
#  |200|200|100|100|100|
#  |___|200|200|200|100|
#
#  _________________________________________
#  |  3|  3|  3|  3|  3|___|___|___|___|___|
#  |  3|  3|  3| 10| 10|  7|  7|  7|___|___|
#  |  3|  3|  3| 10| 10|  8|  8|  8|  1|___|
#


def arrayManipulation(n, queries):
    array_vals = [0] * n

    for i in range(len(queries)):
        min_int = queries[i][0]
        max_int = queries[i][1]
        val = queries[i][2]
        for j in range(min_int-1,max_int):
            array_vals[j] = (array_vals[j]+val)

    return max(array_vals)



n =5
queries = [[1,2,100],[2,5,100],[3,4,100]]
result = arrayManipulation(n,queries)
print(f"Result: {result}")



n = 10
queries = [[1,5,3],[4,8,7],[6,9,1]]
result = arrayManipulation(n,queries)
print(f"Result: {result}")



n = 10
queries = [[2,6,8],[3,5,7],[1,8,1],[5,9,15]]
result = arrayManipulation(n,queries)
print(f"Result: {result}")