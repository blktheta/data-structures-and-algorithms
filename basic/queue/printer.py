"""
Method: Queue
Example: Printing tasks

Algorithm to answer the question whether the current printer could
handle the task load if it were set to print with a better quality but slower
page rate.

As print tasks are submitted, they will be added to a waiting list,
a queue of print tasks atached to the printer.

When the printer completes a task, it will look a the queue to see
if there are any remaining tasks to process.

The interesting part is The average amount of time a person has to wait
for their papers to be printed.

Simulation probabilities:
    1. A person may print a paper from 1 to 20 pages in length. If each
    length from 1 to 20 is equally likely, the length for a print task
    can be simulated by using random numbers between 1 and 20 inclusive.

    2. If there are 10 people in the office and each prints twice,
    then there are 20 prints tasks per hour on average. Which means
    that on average there will be one task every 180 seconds.

    3. For every second we can simulate the chance that a print task
    occurs by generating a random number between 1 and 180 inclusive.
    I the number is 180, we say a task has been created. Note that
    there it is possible that many tasks could be created in a row.
"""
import random

from queue import Queue


class Task:
    """Printing task."""
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def get_stamp(self) -> float:
        """Timestamp for computing watiting time."""
        return self.timestamp

    def get_pages(self) -> int:
        """Random length from 1 to 20 pages."""
        return self.pages

    def wait_time(self, current_time) -> float:
        """Retrieve the amount of time spent in the queue."""
        return current_time - self.timestamp


class Printer:
    """Track current printing tasks."""
    def __init__(self, ppm: int):
        self.page_rate = ppm    # pages-per-minute
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        """Decrement the internal timer. Set the printer to idle."""
        if self.current_task is not None:
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self) -> bool:
        """Track whether printer has a current task."""
        return self.current_task is not None

    def start_next(self, new_task: Task):
        """Track the amount of time needed to finish the task."""
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() * 60 / self.page_rate


def new_print_task() -> bool:
    """Decide whether a new printing task has been created."""
    num = random.randrange(1, 181)
    return num == 180


def simulation(num_seconds: int, pages_per_minute: int):
    """Simulate random evens of printing tasks.

    num_seconds: total runtime of simulation in seconds
    pages_per_minute: average printing tasks per minute
    """
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


def main():
    for _ in range(10):
        # 60 minutes, 3 pages per minute
        simulation(3600, 5)


if __name__ == "__main__":
    main()
