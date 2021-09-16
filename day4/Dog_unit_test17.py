'''
importing unitest
'''
import unittest
#importing Dog
import Dog
class TestBinaryTree(unittest.TestCase):
    '''
    this class inherit unittest Testcase for checking its unit testing
    '''
    def test_0_description(self):
        name = Dog.Dog("browny",12)
        print("test started ")
        self.assertEqual(name.name,"browny")
        print(f" the name  of  dog is  {name.name} ")
        print("test executes smoothly ")
if __name__ == '__main__':
    #running script
    unittest.main()