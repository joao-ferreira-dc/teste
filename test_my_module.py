import unittest
from my_module import my_function

class TestMyFunction(unittest.TestCase):
    def test_valid_input(self):
        self.assertEqual(my_function(2), 4)

if __name__ == '__main__':
    unittest.main()
