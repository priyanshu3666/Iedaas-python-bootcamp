'''
importing unitest
'''
import unittest
#importing Time
import times as TimeClass
class TestTime(unittest.TestCase):
    '''
    this class inherit unittest Testcase for checking its unit testing
    '''
    def test_0_minute_display(self):
        '''
        checking add minutes
        '''
        print("test started ")
        
        minute_display  =TimeClass.Times(4,20).displayMinute()
        self.assertEqual(minute_display,260)
        print(f"total minute are {minute_display} minutes")
        print("test executes smoothly ")
if __name__ == '__main__':
    #running script
    unittest.main()