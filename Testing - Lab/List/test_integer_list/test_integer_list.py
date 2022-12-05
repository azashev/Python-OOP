from unittest import TestCase, main
from integer_list_03 import IntegerList


class TestIntegerList(TestCase):
    def setUp(self):
        self.integer_list = IntegerList(5, 45, 8.3, "10", False)

    def test_correct_initialization(self):
        self.assertIn(5, self.integer_list._IntegerList__data)
        self.assertIn(45, self.integer_list._IntegerList__data)
        self.assertNotIn(8.3, self.integer_list._IntegerList__data)
        self.assertNotIn("10", self.integer_list._IntegerList__data)
        self.assertNotIn(False, self.integer_list._IntegerList__data)

    def test_get_data(self):
        self.assertEqual([5, 45], self.integer_list.get_data())

    def test_add_correct(self):
        result = self.integer_list.add(70)

        self.assertEqual(result, [5, 45, 70])
        self.assertEqual([5, 45, 70], self.integer_list._IntegerList__data)

    def test_add_with_non_int_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.integer_list.add("10")

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_remove_valid_index(self):
        result = self.integer_list.remove_index(1)

        self.assertNotIn(45, self.integer_list._IntegerList__data)
        self.assertEqual(45, result)

    def test_remove_invalid_index_raise_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.remove_index(2)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_get_correct_index(self):
        self.assertEqual(45, self.integer_list.get(1))

    def test_get_incorrect_index(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.get(2)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_correct_insert(self):
        self.integer_list.insert(1, 20)
        self.assertIn(20, self.integer_list._IntegerList__data)

    def test_insert_index_out_of_range_raise_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.insert(2, 20)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_non_int_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.integer_list.insert(1, "10")

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_get_biggest_correct(self):
        self.assertEqual(45, self.integer_list.get_biggest())

    def test_get_index_correct(self):
        self.assertEqual(1, self.integer_list.get_index(45))


if __name__ == '__main__':
    main()
