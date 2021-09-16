'''
importing unitest
'''
import unittest
#importing student
import student
class TestDisplay(unittest.TestCase):
    '''
    this class inherit unittest Testcase for checking its unit testing
    '''
    def test_0_display(self):
        '''
        checking whether function is returning magic string or not 
        '''
        print("test started ")
        student_ =student.Student("Priyanshu",50)
        student_display =student_.display()
        self.assertEqual(student_.name,"Priyanshu")
        print("test executes smoothly ")
if __name__ == '__main__':
    #running script
    unittest.main()