'''
importing unitest
'''
import unittest
#importing greet
import greet
class TestGreet(unittest.TestCase):
    '''
    this class inherit unittest Testcase for checking its unit testing
    '''
    def test_0_greet_with_name(self):
        result = greet.greet("priyanshu")
        print("test started ")
        self.assertEqual(result,"Hello, priyanshu. Good morning!")
        print(result)
        print("test executes smoothly ")
if __name__ == '__main__':
    #running script
    unittest.main()