import unittest

def strings_xor(s, t):
    res = ""
    for i in range(len(s)):
        if s[i] == t[i]:
            res += '0';
        else:
            res += '1';

    return res

class Testes(unittest.TestCase):
    def test_caso_0(self):
        self.assertEqual(strings_xor("10101","00101"),"10000")

if __name__ == "__main__":
    unittest.main()