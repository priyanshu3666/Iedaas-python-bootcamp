'''
importing unitest
'''
import unittest
#importing Integer_to_Roman 
import Integer_to_Roman
class TestRomanConversion(unittest.TestCase):
    '''
    this class inherit unittest Testcase for checking its unit testing
    '''
    def test_0_display(self):
        '''
        checking whether function is returning magic string or not 
        '''
        num = 500
        print("test started ")
        result =Integer_to_Roman.IntegerToRoman.int_to_Roman(self,num)
        self.assertEqual(result,"D")
        print(f" the {num} in roman is {result}")
        print("test executes smoothly ")
if __name__ == '__main__':
    #running script
    unittest.main()