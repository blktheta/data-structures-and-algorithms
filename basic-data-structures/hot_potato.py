from queue import Queue


def hot_potato(names: list, num: int) -> str:
    sim_queue = Queue()
    for name in names:
        sim_queue.enqueue(name)

    while sim_queue.size() > 1:
        for _ in range(num):
            sim_queue.enqueue(sim_queue.dequeue())

        sim_queue.dequeue()

    return sim_queue.dequeue()


print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))
