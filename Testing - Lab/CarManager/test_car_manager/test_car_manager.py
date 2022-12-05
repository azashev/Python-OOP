from unittest import TestCase, main
from car_manager_04 import Car


class TestCarManager(TestCase):
    def setUp(self):
        self.car = Car("Honda", "CRV", 10, 150)

    def test_correct_initialization(self):
        self.assertEqual("Honda", self.car.make)
        self.assertEqual("CRV", self.car.model)
        self.assertEqual(10, self.car.fuel_consumption)
        self.assertEqual(150, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_incorrect_initialization_make_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car = Car("", "CRV", 10, 150)

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_incorrect_initialization_model_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ''

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_incorrect_initialization_fuel_consumption_zero_or_less_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car = Car("Honda", "CRV", 0, 150)

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_incorrect_initialization_fuel_capacity_zero_or_less_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car = Car("Honda", "CRV", 10, 0)

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_incorrect_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_correct_refuel_with_more_fuel_than_capacity(self):
        self.car.refuel(200)

        self.assertEqual(150, self.car.fuel_amount)

    def test_incorrect_refuel_zero_or_less_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_drive_correct(self):
        self.car.fuel_amount = 100
        self.car.drive(20)

        self.assertEqual(98, self.car.fuel_amount)

    def test_drive_incorrect_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(10)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))


if __name__ == "__main__":
    main()
