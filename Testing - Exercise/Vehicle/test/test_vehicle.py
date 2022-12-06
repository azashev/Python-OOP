from unittest import TestCase, main
from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(20.5, 180.5)

    def test_default_fuel_consumption_correct(self):
        self.assertEqual(1.25, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_correct_initialization(self):
        self.assertEqual(20.5, self.vehicle.fuel)
        self.assertEqual(self.vehicle.fuel, self.vehicle.capacity)
        self.assertEqual(180.5, self.vehicle.horse_power)
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_drive_correct(self):
        self.vehicle.drive(10)

        self.assertEqual(8.0, self.vehicle.fuel)

    def test_drive_incorrect_not_enough_fuel_raise_exception(self):
        self.vehicle.fuel = 0

        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(1)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel_increase_fuel_correct(self):
        self.vehicle.fuel = 0
        self.vehicle.refuel(10)

        self.assertEqual(10, self.vehicle.fuel)

    def test_refuel_full_car_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(1)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test__str__correct(self):
        result = str(self.vehicle)

        self.assertEqual("The vehicle has 180.5 horse power with 20.5 fuel left and 1.25 fuel consumption", result)


if __name__ == "__main__":
    main()
