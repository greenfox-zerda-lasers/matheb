import unittest
from Boglarka_Mathe_work import anagramm, count_letters


class week05day1(unittest.TestCase):
    def setUp(self):
        self.anagramm = anagramm("string1", "string2")
        self.count_letters = count_letters("string")

    def test_compare_strings_are_anagramms(self):
        self.assertTrue(anagramm("almas", "malas"))

    def test_compare_strings_are_anagramms(self):
        self.assertTrue(anagramm("a lmas", "malas"))

    def test_compare_strings_are_anagramms(self):
        self.assertTrue(anagramm("Almas", "malas"))

    def test_compare_strings_are_not_anagramms(self):
        self.assertFalse(anagramm("almaska", "malas"))

    def test_compare_strings_are_anagramms_not_strings(self):
        self.assertRaises(ValueError, anagramm, 453, 415)

    def test_compare_strings_are_anagramms_first_arg_not_string(self):
        self.assertRaises(ValueError, anagramm, 3, "alma")

    def test_compare_strings_are_anagramms_second_arg_not_string(self):
        self.assertRaises(ValueError, anagramm, 'three', 3)

    def test_letter_dict_lower_letters(self):
        self.assertEqual(count_letters("almafa"), {'a':3, 'l': 1, 'm':1, 'f':1})

    def test_letter_dict_in_case_of_special_char(self):
        self.assertEqual(count_letters("al1 2 ma+ fa"), {'a':3, 'l': 1, 'm':1, 'f':1})

    def test_letter_dict_upper_letters(self):
        self.assertEqual(count_letters("alMafa"), {'a':3, 'l': 1, 'm':1, 'f':1})

    def test_letter_dict_special_letter(self):
        self.assertEqual(count_letters("alMafá+!"), {'a':2, 'l': 1, 'm':1, 'f':1, 'á':1, })

    def test_count_letters_arg_not_string(self):
        self.assertRaises(ValueError, count_letters, 453)


if __name__ == '__main__':
    unittest.main()
