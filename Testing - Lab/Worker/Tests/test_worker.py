from unittest import TestCase, main
from worker_01 import Worker


class WorkerTests(TestCase):
    def setUp(self):
        self.worker = Worker("TestName", 1000, 100)

    def test_correct_initialization(self):
        self.assertEqual("TestName", self.worker.name)
        self.assertEqual(1000, self.worker.salary)
        self.assertEqual(100, self.worker.energy)

    def test_energy_increment_after_rest_call(self):
        self.worker.rest()
        self.assertEqual(101, self.worker.energy)

    def test_worker_tries_to_work_with_zero_energy(self):
        self.worker.energy = 0
        with self.assertRaises(Exception) as ex:
            self.worker.work()
        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_worker_salary_increases_after_working(self):
        self.worker.work()
        self.assertEqual(self.worker.salary, self.worker.money)

    def test_worker_energy_decreases_after_working(self):
        self.worker.work()
        self.assertEqual(99, self.worker.energy)

    def test_get_info_method(self):
        self.assertEqual("TestName has saved 0 money.", self.worker.get_info())


if __name__ == '__main__':
    main()
