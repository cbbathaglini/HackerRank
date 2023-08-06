#https://www.hackerrank.com/challenges/breaking-best-and-worst-records/submissions/code/339488718
def breakingRecords(scores):
    arr_highests = []
    arr_lowests = []
    maior = scores[0]
    menor = scores[0]
    arr_final =[]
    for i in range(len(scores)):
        if scores[i] > maior:
            maior = scores[i]
            arr_lowests.append(scores[i])
        if scores[i] < menor:
            menor = scores[i]
            arr_highests.append(scores[i])
    #print(f"high: {arr_highests}")
    #print(f"low: {arr_lowests}")
    #print(f"high: {len(arr_highests)}")
    #print(f"low: {len(arr_lowests)}")
    
    arr_final.append(len(arr_lowests))
    arr_final.append(len(arr_highests))
    return arr_final