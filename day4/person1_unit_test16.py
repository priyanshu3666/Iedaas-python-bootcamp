'''
importing unitest
'''
import unittest
#importing Person1
import person1
class TestPhoneNumber(unittest.TestCase):
    '''
    this class inherit unittest Testcase for checking its unit testing
    '''
    def test_0_get_phoneNumber(self):
        phone= person1.Person("Priyanshu","shukla",8004954515,'ps7080895123@gmail.com')
        print("test started ")
        result =phone.get_phone()
        self.assertEqual(result,8004954515)
        print(f" the {phone.name} {phone.surname}  has teleephone number which is {result}")
        print("test executes smoothly ")
if __name__ == '__main__':
    #running script
    unittest.main()