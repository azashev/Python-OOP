from abc import abstractmethod
import time


class WorkMixin:
    @abstractmethod
    def work(self):
        pass


class EatMixin:
    @abstractmethod
    def eat(self):
        pass


class Worker(WorkMixin, EatMixin):
    def work(self):
        print("I'm normal worker. I'm working.")

    def eat(self):
        print("Lunch break....(5 secs)")
        time.sleep(5)


class SuperWorker(WorkMixin, EatMixin):
    def work(self):
        print("I'm super worker. I work very hard!")

    def eat(self):
        print("Lunch break....(3 secs)")
        time.sleep(3)


class Robot(WorkMixin):
    def work(self):
        print("I'm a robot. I'm working....")


class Manager:
    def __init__(self):
        self.worker = None

    @abstractmethod
    def set_worker(self, worker):
        pass


class WorkManager(Manager):
    def set_worker(self, worker):
        assert isinstance(worker, WorkMixin), f"`worker` must be of type {WorkMixin}"

        self.worker = worker

    def manage(self):
        self.worker.work()


class BreakManager(Manager):
    def set_worker(self, worker):
        assert isinstance(worker, EatMixin), f"`worker` must be of type {EatMixin}"

        self.worker = worker

    def lunch_break(self):
        self.worker.eat()


# Test code:
work_manager = WorkManager()
break_manager = BreakManager()
work_manager.set_worker(Worker())
break_manager.set_worker(Worker())
work_manager.manage()
break_manager.lunch_break()

work_manager.set_worker(SuperWorker())
break_manager.set_worker(SuperWorker())
work_manager.manage()
break_manager.lunch_break()

work_manager.set_worker(Robot())
work_manager.manage()
try:
    break_manager.set_worker(Robot())
    break_manager.lunch_break()
except:
    pass

# Expected output:
# I'm normal worker. I'm working.
# Lunch break....(5 secs)
# I'm super worker. I work very hard!
# Lunch break....(3 secs)
# I'm a robot. I'm working....
