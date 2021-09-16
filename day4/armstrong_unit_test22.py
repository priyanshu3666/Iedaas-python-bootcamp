'''
import unittest
'''
import unittest
import armstrong

class TestFibbonaci(unittest.TestCase):
    def test_0_armstrong(self):
        result =armstrong.IsArmstrong()
        print("test started ")
        self.assertEquals(result,False)
        print(result)
        print("program executes smoothly")

if __name__ == '__main__':
    #running script
    unittest.main()