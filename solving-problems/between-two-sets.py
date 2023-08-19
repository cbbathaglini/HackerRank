import unittest
#x%2 == 0 and x%6==0 and 24%x == 0 and 36%x==0
def getTotalX(a, b):   
   
    arr_factors =[]
    #gera lista de fatores
    for j in range(1,max(b)+1):
        ambos = 0
        for i in range(len(a)):
            if j % a[i] == 0:
                ambos +=1
        if ambos == len(a):
            arr_factors.append(j)
    
    #print(f"{arr_factors}")  
                              
    arr_factors_final = []
    for j in range(len(arr_factors)):
        ambos = 0
        for i in range(len(b)):
            if b[i] % arr_factors[j] == 0:
                ambos +=1
        if ambos == len(b):
            arr_factors_final.append(arr_factors[j])
                    
    #print(f"{arr_factors_final}")
    
    return len(arr_factors_final)


class Testes(unittest.TestCase):
    def test_caso_1(self):
        a = [2, 4]
        b = [16, 32, 96]
        self.assertEqual(getTotalX(a,b),3)
    
    def test_caso_2(self):
        a = [2, 6]
        b = [24,36]
        self.assertEqual(getTotalX(a,b),2)
    
    def test_caso_3(self):
        a = [3, 4]
        b = [24, 48]
        self.assertEqual(getTotalX(a,b),2)
    
    def test_caso_4(self):
        a = [1]
        b = [100]
        self.assertEqual(getTotalX(a,b),9)


if __name__ == "__main__":
    unittest.main()