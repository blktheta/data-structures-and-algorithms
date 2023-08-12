"""
Method: Queue
Example: Hot potato

Algorithm that read a list of names and constant, then return the last
person remaining after repetitive counting by the constant.

The children's game hot potato, requires children to line up in a circle
and pass an item from neighbor to neighbor as fast as they can. At a
certain point in the game, the action is stopped and the child who has
the item (the potato) is removed from the circle. Play continues until
only one chils is left.

Participants: [Bill, David, Susan, Jane, Kent, Brad]
Constant: 5
Round 1:

                    Bill                Bill    passes to David
                ->        ->            David   passes to Susan
           (Brad)           David       Susan   passes to Jane
              ^               |         Jane    passes to Kent
              |               v         Kent    passes to Brad
            Kent            Susan       After 5 passes Brad is eliminated
                <-        <-
                    Jane

Round 2:
           (Bill)   --->    David       Bill    passes to David
              ^               |         David   passes to Susan
              |               v         Susan   passes to Jane
            Kent            Susan       Jane    passes to Kent
                <-        <-            Kent    passes to Bill
                    Jane                After 5 passes Bill is eliminated

... and so on.

"""
from queue import Queue


def hot_potato(names: list, num: int) -> str:
    """ Return the name of the last person remaining.

    Simulation of Hot Potato, the last named return is
    based on repetative counting of num.
    """
    sim_queue = Queue()
    for name in names:
        sim_queue.enqueue(name)

    while sim_queue.size() > 1:
        for _ in range(num):
            sim_queue.enqueue(sim_queue.dequeue())

        sim_queue.dequeue()

    return sim_queue.dequeue()


def main():
    print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))
    print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 24))

if __name__ == "__main__":
    main()
