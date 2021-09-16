'''
import unittest
'''
import unittest
import list_product

class TestListOfProduct(unittest.TestCase):
    def test_0_get_list_of_products(self):
        list_=[1,2,3]
        result =list_product.list_product(list_)
        print("test started ")
        self.assertIsNotNone(result)
        print(result)
        print("program executes smoothly")

if __name__ == '__main__':
    #running script
    unittest.main()