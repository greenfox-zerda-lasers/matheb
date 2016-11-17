import unittest
import third

class TestExtend(unittest.TestCase):

    def test_birth_date_input_is_invalid(self):
        person = third.Person('Eric', 2017)
        self.assertRaises(PermissionError, person.check_birth_date, 0)

    def test_birth_date_input_not_int(self):
        person = third.Person('Eric', 'three')
        self.assertRaises(ValueError, person.check_birth_date, 'three')

    def test_birth_date_is_valid(self):
        person = third.Person('Eric', 2000)
        self.assertEqual(person.check_birth_date, 2000)

if __name__ == '__main__':
    unittest.main()
