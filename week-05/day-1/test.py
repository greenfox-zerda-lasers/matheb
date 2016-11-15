import unittest
import extend

class TestExtend(unittest.TestCase):

    """---------TEST of ADD function ---------------"""
    def test_add_2_and_3_is_5(self):
        self.assertEqual(extend.add(5, 3), 8)

    def test_add_4_and_1_is_5(self):
        self.assertEqual(extend.add(4, 1), 5)

    def test_add_input_str(self):
        self.assertRaises(ValueError, extend.add, 'borso', 'alma')

    def test_add_input_second_string(self):
        self.assertRaises(ValueError, extend.add, 3, "alma")

    def test_add_input_first_string(self):
        self.assertRaises(ValueError, extend.add, 'three', 3)

    """---------TEST of MAX of THREE function ---------------"""
    def test_max_of_three_first(self):
        self.assertEqual(extend.max_of_three(4, 6, 3), 6)

    def test_max_of_three_third(self):
        self.assertEqual(extend.max_of_three(3, 4, 5), 5)

    def test_max_of_three_input_str(self):
        self.assertRaises(ValueError, extend.max_of_three, 'borso', 'alma', 'szolo')

    def test_max_of_three_input_second_string(self):
        self.assertRaises(ValueError, extend.max_of_three, 3, "alma", 4)

    def test_maxof_three_input_first_string(self):
        self.assertRaises(ValueError, extend.max_of_three, 'three', 3, 6)

    def test_maxof_three_input_third_string(self):
        self.assertRaises(ValueError, extend.max_of_three, 3, 6, 'bla')

    """---------TEST of MEDIAN function ---------------"""
    def test_median_four(self):
        self.assertEqual(extend.median([7,4,3,5,]), 4.5)

    def test_median_five(self):
        self.assertEqual(extend.median([1,2,2,4,5]), 2)

    def test_median_input_string(self):
        self.assertRaises(ValueError, extend.median, 'bla+!')

    def test_median_input_float(self):
        self.assertRaises(ValueError, extend.median, [3.2, 3])

    """---------TEST of ISVOVEL function ---------------"""
    def test_is_vovel_o(self):
        self.assertTrue(extend.is_vovel('o'))

    def test_is_vovel_special_char(self):
        self.assertFalse(extend.is_vovel('+'))

    def test_is_vovel_input_type(self):
        self.assertRaises(TypeError, extend.is_vovel, 452)

    def test_is_vovel_input_type(self):
        self.assertRaises(ValueError, extend.is_vovel, 'klm')

    """---------TEST of TRANSLATE function ---------------"""
    def test_translate_bemutatkozik(self):
        self.assertEqual(extend.translate('bemutatkozik'), 'bevemuvutavatkovozivik')

    def test_translate_kolbice(self):
        self.assertEqual(extend.translate('kolbice'), 'kovolbiviceve')

    def test_translate_input_type_int(self):
        self.assertRaises(TypeError, extend.translate, 452)

    def test_translate_number_between_letters(self):
        self.assertRaises(TypeError, extend.translate, 'k3lm')

    def test_translate_empty_input(self):
        self.assertRaises(TypeError, extend.translate, ' ')

if __name__ == '__main__':
    unittest.main()
