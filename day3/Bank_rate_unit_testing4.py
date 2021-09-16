import unittest
import Bank_rate as  BankClass

class Policy(unittest.TestCase):
    '''
    this class inherit unittest
    '''
    def test_best_policy(self):      
        '''This method  fetch the bank name with best rate of intrest
        '''
        print("best policy test started")
        Bank_ = BankClass.Bank()
        if Bank_.get_BOB()>Bank_.get_PNB():
            print(" BOB gives best policy. its rate is {}".format(Bank_.get_BOB()))
        else:
            if  Bank_.get_SBI()>Bank_.get_PNB():
                print("SBI gives best policy. its rate is {}".format(Bank_.get_SBI()))
            else :
                print("PNB gives best policy. its rate is {}".format(Bank_.get_PNB()))
        print("best policy  test ended ")
    
if __name__ == '__main__':
    unittest.main()