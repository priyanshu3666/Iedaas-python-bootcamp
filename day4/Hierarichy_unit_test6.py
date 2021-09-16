'''
importing unitest
'''
import unittest
#importing hierarichy as H_Class
import hierarichical as H_Class
class TestHierarchy(unittest.TestCase):
    '''
    this class inherit unittest Testcase for checking its unit testing
    '''
    def test_0_is_child(self):
        '''
        checking whether two child classes inheriting same class or not
        '''
        object1 = H_Class.Child1()
        object2 = H_Class.Child2()
        #checking two function of different class to be same or not
        self.assertEqual(object1.func1(), object2.func1())
if __name__ == '__main__':
    #running script
    unittest.main()
