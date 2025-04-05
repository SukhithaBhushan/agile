import unittest

def add_numbers(a,b):
    return a+b
class TestAddition(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add_numbers(1,2),3)
        self.assertEqual(add_numbers(1,2),3)
        self.assertEqual(add_numbers(1,2),3)
        self.assertEqual(add_numbers(1,2),3)
if __name__=="__main__":
    unittest.main()
