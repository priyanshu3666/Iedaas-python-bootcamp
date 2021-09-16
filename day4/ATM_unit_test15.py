'''
importing unitest
'''
import unittest
#importing ATM
import ATM
class TestRomanConversion(unittest.TestCase):
    '''
    this class inherit unittest Testcase for checking its unit testing
    '''
    def test_0_withdrawl(self):
        '''
        checking whether ATM dispense money or not 
        '''
        atm = ATM.ATM("priyanshu",10000)
        print("test started ")
        atm.withdrawl(4000)
        result =atm.balance
        self.assertEqual(result,6000)
        print(f"  ATM currentt balance is {atm.balance}")
        print("test executes smoothly ")
if __name__ == '__main__':
    #running script
    unittest.main()