import unittest

def countingValleys(steps, path):
    valleys, level , val = 0, 0, 0
    arr_levels = []
    for i in range(steps):
        if path[i] == 'U': val = 1
        if path[i] == 'D': val = -1
        
        level +=val
        arr_levels.append(level)
        
    for i in range(steps-1):
        if arr_levels[len(arr_levels)-1] == 0:
            if (arr_levels[i] == -1 and arr_levels[i+1]==0) or (arr_levels[i] == 0 and arr_levels[i+1]==-1) and (arr_levels[i+1]==0 and not i == len(arr_levels)-2):
                valleys +=1
 
    return valleys



class TestesSteps(unittest.TestCase):
    def test_caso_0(self):
        # DUDDDUUDUU
        # _          _
        #  \/\      /
        #     \  /\/ 
        #      \/
        #
        # [-1, 0, -1, -2, -3, -2, -1, -2, -1, 0]
        steps= 10
        path = ['D','U','D','D','D','U','U','D','U','U']
        self.assertEqual(countingValleys(steps, path),3)

    def test_caso_1(self):
        # UDDDUDUU
        #  
        # _/\      _
        #    \    /
        #     \/\/
        #
        steps = 8
        path = ['U','D','D','D','U','D','U','U']
        self.assertEqual(countingValleys(steps, path),1)

    def test_caso_2(self):

        # DDUUDDUDUUUD
        #
        # _          /\_ 
        #  \  /\    /
        #   \/  \/\/
        #
        # 
        steps = 12
        path = ['D','D','U','U','D','D','U','D','U','U','U','D']
        self.assertEqual(countingValleys(steps, path),2)


if __name__ == "__main__":
    unitest.main()