#https://www.hackerrank.com/challenges/mini-max-sum/submissions/code/339044855
import unittest

# find the minimum and maximum values that can be calculated by summing exactly four of the five integers
def miniMaxSum(arr):
    arr.sort()
    #print(f"{sum(arr[0:4])} {sum(arr[1:5])}")
    return [sum(arr[0:4]),sum(arr[1:5])]
    



class TestsMiniMaxSum(unittest.TestCase):
    def test_case_0(self):
        result = miniMaxSum([1,2,3,4,5])
        self.assertEqual(result, [10,14])

    def test_case_1(self):
        result = miniMaxSum([7,69,2,221,8974])
        self.assertEqual(result, [299,9271])

    

if __name__ == '__main__':
    unittest.main()
