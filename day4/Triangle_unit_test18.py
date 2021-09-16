'''
importing unitest
'''
import unittest
#importing Equilateral
import Triangle
class TestTriangle(unittest.TestCase):
    '''
    this class inherit unittest Testcase for checking its unit testing
    '''
    def test_0_check_triangle(self):
        my_triangle=Triangle.Triangle(90,30,60)
        
        print("test started ")
        self.assertTrue(my_triangle.check_angles())
        print(f" it  is an triangle")
        print("test executes smoothly ")
if __name__ == '__main__':
    #running script
    unittest.main()