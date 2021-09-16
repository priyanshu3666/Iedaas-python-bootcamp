'''
importing unitest
'''
import unittest
#importing Temperatue
import Temperature
class TestString(unittest.TestCase):
    '''
    this class inherit unittest Testcase for checking its unit testing
    '''
    def test_0_fahrenhiet_to_celcius(self):
        '''
        checking whether function is returning magic string or not 
        '''
        print("test started ")
        fahrenhiet =98.7
        new_celcius =Temperature.Temprature.convertCelsius(self,fahrenhiet)
        self.assertEqual(new_celcius,37.05)
        print(f"converted celcius {new_celcius} C")
        print("test executes smoothly ")
if __name__ == '__main__':
    #running script
    unittest.main()