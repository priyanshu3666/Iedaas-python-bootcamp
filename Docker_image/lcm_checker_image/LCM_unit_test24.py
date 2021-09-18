'''
import unittest
'''
import unittest
import LCM

class TestLCM(unittest.TestCase):
    def test_0_get_LCM(self):
        result =LCM.calculate_lcm(12,60)
        print("test started ")
        self.assertEqual(result,60)
        print(result)
        print("program executes smoothly")

if __name__ == '__main__':
    #running script
    unittest.main()