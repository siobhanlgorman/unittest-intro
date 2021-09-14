import unittest
from evens import even_number_of_evens


class TestEvens(unittest.TestCase):
    def test_throws_error_if_value_passed_in_is_not_list(self):
        self.assertRaises(TypeError, even_number_of_evens, 4)


if __name__ == '__main__':
    unittest.main()
