'''
import unittest
'''
import unittest
import pallindrome

class Testpallindrome(unittest.TestCase):
    def test_0_pallindrome(self):
        result =pallindrome.isPallindrome(454)
        print("test started ")
        self.assertEquals(result,True)
        print(result)
        print("program executes smoothly")

if __name__ == '__main__':
    #running script
    unittest.main()