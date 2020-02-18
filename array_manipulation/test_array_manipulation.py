import unittest

from array_manipulation import array_manipulation


class TestArrayManipulation(unittest.TestCase):
    def test_simple_array_one_operation(self):
        queries = [[1, 2, 1]]
        number_of_columns = 2
        result = array_manipulation(number_of_columns, queries)

        self.assertEqual(1, result)

    def test_simple_array_two_operations(self):
        queries = [[1, 2, 1], [1, 2, 1]]
        number_of_columns = 2
        result = array_manipulation(number_of_columns, queries)

        self.assertEqual(2, result)
