import unittest
# 0 1 1 2 3 5 8

def fibonnaci(n):
    if n <= 1 and n >= 0:
        return n

    return fibonnaci(n-1) + fibonnaci(n-2)


class TestesFibonnaci(unittest.TestCase):
    def test_caso_0(self):
        self.assertEqual(fibonnaci(0),0)

    def test_caso_1(self):
        self.assertEquals(fibonnaci(1),1)

    def test_caso_3(self):
        self.assertEquals(fibonnaci(3),2)

    def test_caso_8(self):
        self.assertEquals(fibonnaci(6),8)

if __name__ == "__main__":
    unittest.main()