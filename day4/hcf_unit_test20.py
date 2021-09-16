'''
import unittest
'''
import unittest
import hcf

class TestHCF(unittest.TestCase):
    def test_0_HCF(self):
        result =hcf.hcf(5,20)
        print("test started ")
        self.assertTrue(result,12)
        print(result)
        print("program executes smoothly")

if __name__ == '__main__':
    #running script
    unittest.main()