import unittest


def birthday(s, d, m):
    
    
    i, i_aux, soma,ok = 0,0,0,0
    
    if i == len(s)-1 :
        for j in range(m):
            soma += s[i]  
        if soma == d:
            ok =1
    
    
    while i < len(s)-1:
        soma = 0
        for j in range(m):
            soma += s[i]
            i+=1 
            if i == len(s): break
                
        if soma == d:
            ok +=1
        i_aux +=1
        i = i_aux    
    
    
    return ok


class Testes(unittest.TestCase):
    def test_caso_0(self):
        s = [2 ,5 ,1 ,3 ,4 ,4 ,3 ,5 ,1 ,1 ,2 ,1 ,4 ,1 ,3 ,3 ,4 ,2 ,1] 
        d = 18
        m = 7
        self.assertEqual(birthday(s, d, m),3)

    def test_caso_1(self):
        s = [1 ,2 ,1 ,3 ,2] 
        d = 3
        m = 2
        self.assertEqual(birthday(s, d, m),2)

    def test_caso_2(self):
        s = [1 ,1 ,1 ,1 ,1, 1] 
        d = 3
        m = 2
        self.assertEqual(birthday(s, d, m),0)
    
    def test_caso_3(self):
        s = [4] 
        d = 4
        m = 1
        self.assertEqual(birthday(s, d, m),1)

if __name__ == "__main__":
    unittest.main()