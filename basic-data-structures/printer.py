import random

from queue import Queue


"""
Printer simulation to answer the question whether the current printer could
handle the task load if it were set to print with a better quality but slower
page rate. The approach took was to write a simulation that modeled the
printing tasks as random events of various lengths and arrival times.
"""


class Printer:
    def __init__(self, ppm):
        self.page_rate = ppm    # pages-per-minute
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        if self.current_task is not None:
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):
        return self.current_task is not None

    def start_next(self, new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() * 60 / self.page_rate


class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def get_stamp(self):
        return self.timestamp

    def get_pages(self):
        return self.pages

    def wait_time(self, current_time):
        return current_time - self.timestamp


def simulation(num_seconds, pages_per_minute):
    lab_printer = Printer(pages_per_minute)
    print_queue = Queue()
    waiting_times = []

    for current_second in range(num_seconds):
        if new_print_task():
            task = Task(current_second)
            print_queue.enqueue(task)

        if (not lab_printer.busy()) and (not print_queue.is_empty()):
            next_task = print_queue.dequeue()
            waiting_times.append(next_task.wait_time(current_second))
            lab_printer.start_next(next_task)

        lab_printer.tick()

    average_wait = sum(waiting_times) / len(waiting_times)
    print(
        f"Average Wait {average_wait:6.2f} secs"
        + f"{print_queue.size():3d} task remaining."
    )


def new_print_task():
    num = random.randrange(1, 181)
    return num == 180


for _ in range(10):
    # 60 minutes, 3 pages per minute
    simulation(3600, 3)
