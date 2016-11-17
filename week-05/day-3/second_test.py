import unittest
import second

class TestExtend(unittest.TestCase):

    def test_input_is_invalid_file(self):
        self.assertRaises(IOError, second.countLines, 'bla')

if __name__ == '__main__':
    unittest.main()
