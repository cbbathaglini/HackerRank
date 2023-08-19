import unittest

def cutTheSticks(arr):
    
    num = 0
    arr_sticks_cut = []
    arr_sticks_cut.append(len(arr))
    while len(arr) > 0:
        arr = [x - min(arr) for x in arr]
        sobrou = len(arr) - arr.count(0)
        if sobrou == 0: break
        arr_sticks_cut.append(sobrou)
        arr = [x for x in arr if x != 0]

    return arr_sticks_cut    


class Testes(unittest.TestCase):
    def test_caso_0(self):
        self.assertEqual(cutTheSticks([1,2,3,4,3,3,2,1]),[8,6,4,1])

    def test_caso_1(self):
        self.assertEqual(cutTheSticks([5,4,4,2,2,8]),[6,4,2,1])

    def test_caso_2(self):
        self.assertEqual(cutTheSticks([1,2,3]),[3,2,1])


if __name__ == "__main__":
    unittest.main()