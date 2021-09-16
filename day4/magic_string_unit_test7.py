'''
importing unitest
'''
import unittest
#importing hmagic_string
import magic_string
class TestString(unittest.TestCase):
    '''
    this class inherit unittest Testcase for checking its unit testing
    '''
    def test_0_magic_string(self):
        '''
        checking whether function is returning magic string or not 
        '''
        print("test started ")
        new_string =magic_string.magic_string(string_input='priyanshu')
        self.assertEqual(new_string,"PrIyAnShU")
        print(f"method returns {new_string}")
        print("test executes smoothly ")
if __name__ == '__main__':
    #running script
    unittest.main()