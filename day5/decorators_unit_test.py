import unittest
import decorators

class TestDecorator(unittest.TestCase):
    def test_decorator(self):
        
        decorator_ = decorators.num()
        self.assertEqual(decorator_,400)

if __name__ == '__main__':
    unittest.main()
