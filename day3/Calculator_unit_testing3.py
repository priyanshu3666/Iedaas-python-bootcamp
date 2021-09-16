import unittest
#importing calcultor 
import Calculator as CalculatorClass

class SalaryCalculator(unittest.TestCase):
    '''
    The basic class that inherits unittest.TestCase
    '''
      

    def test_0_calculate_net_salary(self):
        '''
        this method is used to test net salary calcultor
        '''
        print("calculate slary test started")
        calculator = CalculatorClass.Calcultor()
        salary  ='' # initialize salary list   
        base_salary =int(input("enter base salary"))
        hra = int(input("enter hra"))
        pf = int(input("enter pf"))
        salary = calculator.subtract(calculator.add(hra,base_salary),pf) #calculating base salary 
        print("the  net salary is ",salary)
        print("test 0 ended")

if __name__ == '__main__':
    unittest.main()