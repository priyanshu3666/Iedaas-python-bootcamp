'''
importing unitest
'''
import unittest
#importing Circle
import circle
class TestArea(unittest.TestCase):
    '''
    this class inherit unittest Testcase for checking its unit testing
    '''
    def test_0_area_of_circle(self):
        '''
        checking whether function is returning magic string or not 
        '''
        print("test started ")
        radius = 5
        circle_ = circle.Circle(radius)
        area =circle_.getArea() 
        self.assertEqual(area,78.5)
        print(f"area of circle is  {area} ")
        print("test executes smoothly ")
if __name__ == '__main__':
    #running script
    unittest.main()