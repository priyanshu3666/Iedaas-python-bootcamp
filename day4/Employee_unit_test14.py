'''
importing unitest
'''
import unittest
#importing Employee
import Employee
class TestRomanConversion(unittest.TestCase):
    '''
    this class inherit unittest Testcase for checking its unit testing
    '''
    def test_0_employee_detail(self):
        '''
        checking whether employee detail is right or not 
        '''
        employee1 =Employee.Employee("priyanshu",22)
        print("test started ")
        result =employee1.name
        self.assertEqual(result,"priyanshu")
        print(f"  {result} is an employee and his age is {employee1.age}")
        print("test executes smoothly ")
if __name__ == '__main__':
    #running script
    unittest.main()