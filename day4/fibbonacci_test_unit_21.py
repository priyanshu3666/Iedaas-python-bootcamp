'''
import unittest
'''
import unittest
import fibbonacci

class TestFibbonaci(unittest.TestCase):
    def test_0_fibbinacci(self):
        result =fibbonacci.fibonacci(5)
        print("test started ")
        self.assertTrue(result,5)
        print(result)
        print("program executes smoothly")

if __name__ == '__main__':
    #running script
    unittest.main()