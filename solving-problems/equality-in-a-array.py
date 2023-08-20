import unittest

def equalizeArray(arr):
    maior, maior_val = -1, -1
    arr_repetead  = []
    for i in range(len(arr)):
        if arr.count(arr[i]) >= maior:
            maior = arr.count(arr[i])
            maior_val = arr[i]
    
    for i in range(len(arr)):
        if arr[i] == maior_val:
            arr_repetead.append(maior_val)
    
    return abs(len(arr) - len(arr_repetead))



class Testes(unittest.TestCase):
    def test_caso_0(self):
        self.assertEqual(equalizeArray([3,3,2,1,3]),2)
    
    def test_caso_1(self):
        self.assertEqual(equalizeArray([1,2,3,1,2,3,3,3]),4)
    
    def test_caso_2(self):
        self.assertEqual(equalizeArray([1,2,2,3]),2)

if __name__ == "__main__":
    unittest.main()