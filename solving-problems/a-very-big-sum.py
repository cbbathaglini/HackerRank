#https://www.hackerrank.com/challenges/a-very-big-sum/submissions/code/339022705
def aVeryBigSum(ar,ar_count):
    soma = 0
    for i in range(ar_count):
        soma += ar[i]
    return soma