from unittest import TestCase, main
from unittesting.project.plantation import Plantation


class TestPlantation(TestCase):
    def setUp(self):
        self.plantation = Plantation(10)
        self.plantation.workers = ["TestWorker"]

    def test_correct_initialization(self):
        self.assertEqual(10, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual(["TestWorker"], self.plantation.workers)

    def test_setter_non_positive_number_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation = Plantation(-1)

        self.assertEqual("Size must be positive number!", str(ve.exception))

    def test_hire_worker_if_already_added_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.hire_worker("TestWorker")

        self.assertEqual("Worker already hired!", str(ve.exception))

    def test_hire_worker_correct_and_returns_message(self):
        result = self.plantation.hire_worker("TestWorker2")

        self.assertEqual("TestWorker2 successfully hired.", result)
        self.assertEqual(["TestWorker", "TestWorker2"], self.plantation.workers)

    def test__len__method(self):
        self.plantation.plants = {"TestWorker": "TestPlant", "TestWorker2": "TestPlant"}
        result = len(self.plantation)

        self.assertEqual(18, result)

    def test_planting_if_worker_does_not_exist_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("TestWorker2", "TestPlant")

        self.assertEqual("Worker with name TestWorker2 is not hired!", str(ve.exception))

    def test_planting_if_size_is_full_raise_value_error(self):
        self.plantation.plants = {"TestWorker": "TestPlant001"}

        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("TestWorker", "TestPlant01")

        self.assertEqual("The plantation is full!", str(ve.exception))

    def test_planting_with_correct_size_if_worker_exists_and_returns_message(self):
        self.plantation.plants = {"TestWorker": []}
        result = self.plantation.planting("TestWorker", "TestPlant1")

        self.assertEqual("TestWorker planted TestPlant1.", result)
        self.assertEqual({'TestWorker': ['TestPlant1']}, self.plantation.plants)

    def test_planting_correct_size_if_worker_does_not_exist_and_returns_message(self):
        self.plantation.workers = ["TestWorker2"]
        result = self.plantation.planting("TestWorker2", "TestPlant1")

        self.assertEqual("TestWorker2 planted it's first TestPlant1.", result)
        self.assertEqual({'TestWorker2': ['TestPlant1']}, self.plantation.plants)

    def test_two_plantings(self):
        self.plantation.planting("TestWorker", "Test1")
        self.plantation.planting("TestWorker", "Test2")
        self.assertEqual(2, len(self.plantation.plants['TestWorker']))

    def test__str__method(self):
        self.assertEqual("Plantation size: 10\nTestWorker", str(self.plantation))

    def test__repr__method(self):
        self.assertEqual("Size: 10\nWorkers: TestWorker", repr(self.plantation))


if __name__ == "__main__":
    main()
