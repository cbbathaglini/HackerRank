#https://www.hackerrank.com/challenges/mini-max-sum/submissions/code/339044855
def miniMaxSum(arr):
    arr.sort()
    print(f"{sum(arr[0:4])} {sum(arr[1:5])}")