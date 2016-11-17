import unittest
import first

class TestExtend(unittest.TestCase):

    def test_add_input_str(self):
        self.assertRaises(ValueError, first.divideTen, 'bla')

    def test_gave_zero(self):
        self.assertRaises(ZeroDivisionError, first.divideTen, 0)

if __name__ == '__main__':
    unittest.main()
