'''
importing unitest
'''
import unittest
#importing Vehicle
import Vehicle
class TestVehicle(unittest.TestCase):
    '''
    this class inherit unittest Testcase for checking its unit testing
    '''
    def test_0_get_tank_capacity(self):
        vehicle= Vehicle.Vehicle('Ford', 'Explorer', 'SUV')
        print("test started ")
        result =vehicle.max_capacity()
        self.assertEqual(result,14)
        print(f" the {vehicle.model}  has max capacity of {result}")
        print("test executes smoothly ")
if __name__ == '__main__':
    #running script
    unittest.main()