from unittest import TestCase, main

from project.bookstore import Bookstore


class TestBookstore(TestCase):
    def setUp(self):
        self.store = Bookstore(10)

    def test_correct_initialization(self):
        self.assertEqual(10, self.store.books_limit)
        self.assertEqual({}, self.store.availability_in_store_by_book_titles)
        self.assertEqual(0, self.store._Bookstore__total_sold_books)

    def test_initialization_books_limit_zero_or_less_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.store = Bookstore(0)

        self.assertEqual("Books limit of 0 is not valid", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.store = Bookstore(-1)

        self.assertEqual("Books limit of -1 is not valid", str(ve.exception))

    def test__len__method(self):
        self.store.availability_in_store_by_book_titles = {"Book1": 1, "Book2": 2}

        result = len(self.store)

        self.assertEqual(3, result)
        self.assertEqual({"Book1": 1, "Book2": 2}, self.store.availability_in_store_by_book_titles)

    def test_receive_book_correct_and_returns_message(self):
        self.store.availability_in_store_by_book_titles = {"Book1": 1}

        result = self.store.receive_book("Book2", 9)

        self.assertEqual("9 copies of Book2 are available in the bookstore.", result)
        self.assertEqual({"Book1": 1, "Book2": 9}, self.store.availability_in_store_by_book_titles)

    def test_receive_book_limit_reached_raises_exception(self):
        self.store.availability_in_store_by_book_titles = {"Book1": 1}
        self.store.books_limit = 1

        with self.assertRaises(Exception) as ex:
            self.store.receive_book("Book1", 1)

        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))
        self.assertEqual({"Book1": 1}, self.store.availability_in_store_by_book_titles)

    def test_receive_existing_book_correct_and_returns_message(self):
        self.store.availability_in_store_by_book_titles = {"Book1": 1}

        result = self.store.receive_book("Book1", 1)

        self.assertEqual("2 copies of Book1 are available in the bookstore.", result)
        self.assertEqual({"Book1": 2}, self.store.availability_in_store_by_book_titles)

    def test_sell_book_if_doesnt_exist_and_raises_exception(self):
        self.store.availability_in_store_by_book_titles = {"Book1": 1, "Book2": 2}

        with self.assertRaises(Exception) as ex:
            self.store.sell_book("Book3", 1)

        self.assertEqual("Book Book3 doesn't exist!", str(ex.exception))
        self.assertEqual({"Book1": 1, "Book2": 2}, self.store.availability_in_store_by_book_titles)

    def test_sell_book_if_copies_not_enough_and_raises_exception(self):
        self.store.availability_in_store_by_book_titles = {"Book1": 1, "Book2": 2}

        with self.assertRaises(Exception) as ex:
            self.store.sell_book("Book1", 2)

        self.assertEqual("Book1 has not enough copies to sell. Left: 1", str(ex.exception))
        self.assertEqual(0, self.store._Bookstore__total_sold_books)
        self.assertEqual({"Book1": 1, "Book2": 2}, self.store.availability_in_store_by_book_titles)

    def test__str__method(self):
        self.store.availability_in_store_by_book_titles = {"Book1": 1, "Book2": 2}
        self.store._Bookstore__total_sold_books = 3

        self.assertEqual("Total sold books: 3\n"
                         "Current availability: 3\n"
                         " - Book1: 1 copies\n"
                         " - Book2: 2 copies", str(self.store))

    def test_sell_book_correct_and_returns_message(self):
        self.store.availability_in_store_by_book_titles = {"Book1": 2}

        result = self.store.sell_book("Book1", 2)

        self.assertEqual("Sold 2 copies of Book1", result)
        self.assertEqual({"Book1": 0}, self.store.availability_in_store_by_book_titles)
        self.assertEqual(2, self.store._Bookstore__total_sold_books)


if __name__ == "__main__":
    main()
