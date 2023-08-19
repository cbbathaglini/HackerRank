import unittest

# solution from another user
def isBalanced(s):
    bracketsStack = []
    
    for i in range (len(s)):
        bracket = s[i]
      
        if open(bracket):
            bracketsStack.append(bracket)
        else:
            if len(bracketsStack) >0 and alterego(bracketsStack[-1]) == bracket:
                bracketsStack.pop()
            else:
                return False
            
    if len(bracketsStack) == 0:
        return True
    
    return False
    
def open(bracket):
    return bracket == "[" or bracket == '{' or bracket == "("

def alterego(s):
    if s == "{":
        return "}"
    if s == "(":
        return ")"
    if s == "[":
        return "]"

# test dev by me 
class IsBalancedTest(unittest.TestCase):
    def test_caso_1(self):
        result = isBalanced("((()[])[])[][]")
        self.assertTrue(result)

    def test_caso_2(self):
        result = isBalanced('(([)])[]()')
        self.assertFalse(result)

    def test_caso_3(self):
        result = isBalanced(']]]][][][[[[')
        self.assertFalse(result)
    
    def test_caso_4(self):
        result = isBalanced(']][[')
        self.assertFalse(result)
    
    def test_caso_5(self):
        result = isBalanced('{([])}')
        self.assertTrue(result)
    
    def test_caso_6(self):
        result = isBalanced('(([(])[])[])()')
        self.assertFalse(result)

    def test_caso_7(self):
        self.assertTrue(isBalanced("([]()())[]()"))

    def test_caso_8(self):
        self.assertTrue(isBalanced("{(([])[])[]}[]"))
        
        


if __name__ == '__main__':
    unittest.main()

