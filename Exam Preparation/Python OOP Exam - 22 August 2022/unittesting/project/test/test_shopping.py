from unittest import TestCase, main

from project.shopping_cart import ShoppingCart


class TestShoppingCart(TestCase):
    def setUp(self):
        self.shopping_cart = ShoppingCart("TestName", 150.50)
        # self.shopping_cart2 = ShoppingCart("", 0.00)

    def test_correct_initialization(self):
        self.assertEqual("TestName", self.shopping_cart.shop_name)
        self.assertEqual(150.50, self.shopping_cart.budget)
        self.assertEqual({}, self.shopping_cart.products)

    def test_initialization_name_first_letter_not_capital_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart2 = ShoppingCart("testName", 150.50)

        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

    def test_initialization_name_non_letters_only_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart2 = ShoppingCart("TestName2", 150.50)

        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

    def test_add_to_cart_correct_and_returns_message(self):
        result = self.shopping_cart.add_to_cart("TestProduct", 50.50)

        self.assertEqual("TestProduct product was successfully added to the cart!", result)
        self.assertEqual({'TestProduct': 50.50}, self.shopping_cart.products)

    def test_add_to_cart_price_too_high_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.add_to_cart("TestProduct", 100.50)

        self.assertEqual("Product TestProduct cost too much!", str(ve.exception))

    def test_remove_from_cart_correct_and_returns_message(self):
        self.shopping_cart.products = {"TestProduct": 50.50, "TestProduct2": 20}
        result = self.shopping_cart.remove_from_cart("TestProduct")

        self.assertEqual("Product TestProduct was successfully removed from the cart!", result)
        self.assertEqual({"TestProduct2": 20}, self.shopping_cart.products)

    def test_remove_from_cart_incorrect_product_name_raise_value_error(self):
        self.shopping_cart.products = {"TestProduct": 50.50}

        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.remove_from_cart("TestProduct2")

        self.assertEqual("No product with name TestProduct2 in the cart!", str(ve.exception))
        self.assertEqual({"TestProduct": 50.50}, self.shopping_cart.products)

    def test__add__method(self):
        self.shopping_cart.products = {"TestProduct": 50.50, "TestProduct2": 10}
        self.shopping_cart2 = ShoppingCart("TestNameTwo", 120.50)
        self.shopping_cart2.products = {"TestProduct3": 20}

        new_name = self.shopping_cart + self.shopping_cart2

        self.assertEqual("TestNameTestNameTwo", new_name.shop_name)
        self.assertEqual({"TestProduct": 50.50, "TestProduct2": 10, "TestProduct3": 20}, new_name.products)
        self.assertEqual(271, new_name.budget)

    def test_buy_products_correct_and_returns_message(self):
        self.shopping_cart.products = {"TestProduct": 50, "TestProduct2": 10}

        result = self.shopping_cart.buy_products()

        self.assertEqual("Products were successfully bought! Total cost: 60.00lv.", result)

    def test_buy_products_not_enough_budget_raise_value_error(self):
        self.shopping_cart.products = {"TestProduct": 50, "TestProduct2": 50, "TestProduct3": 80}

        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.buy_products()

        self.assertEqual("Not enough money to buy the products! Over budget with 29.50lv!", str(ve.exception))


if __name__ == "__main__":
    main()
