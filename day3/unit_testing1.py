'''
importing unittesting module '''
import unittest

class TestStringMethods(unittest.TestCase):
    '''
    this class inherit unittest Testcase
    '''
    def test_upper(self):
        '''
        checks both strings are equal or not
        '''
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        '''
        checks both strings are upper or not
        '''
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        '''
        this method is spliting the given string
        '''
        string_ = 'hello world'
        self.assertEqual(string_.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            string_.split(2)

if __name__ == '__main__':
    #script running
    unittest.main()
    