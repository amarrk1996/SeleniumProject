import unittest

class TestCase1(unittest.TestCase):

    def test1_useCamelCaseMethodName(self):
        print('test_1 executed and passed')

# we need define above function as a main function
if __name__== 'main':
    unittest.main()