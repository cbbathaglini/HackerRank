#https://www.hackerrank.com/challenges/simple-array-sum/submissions/code/339022623
def simpleArraySum(ar,ar_count):
    soma = 0
    for i in range(ar_count):
        soma += ar[i]
    return soma