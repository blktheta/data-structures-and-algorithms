"""
Tower of Hanoi puzzle

Transfer all disks from one of the three poles to another, with two important
constraints. You can only move one disk at a time, and you can never place a
larger disk on top of a smaller one.

    |           |           |
    |           #           |
    |          ###          |
    |         #####         |
#########    #######        |

from_pole    with_pole    to_pole

Here is a high-level outline of how to move a tower of height H from
the starting pole to the goal pole, using an intermediate pole:

    1. Move a tower of height (H - 1) from the starting pole to an
    intermediate pole via the goal pole.

    2. Move the remaining disk from the starting pole to the final pole.

    3. Move the tower of height (H - 1) from the intermediate pole to
    the goal pole via the starting pole.

The only thing missing from the outline is the base case. The simplest
Tpwer pf Hanoi problem is a tower of one disk.
"""


def move_tower(height: int, from_pole: str, to_pole: str, with_pole: str):
    """Algorithm logic behind Tower of Hanoi.

    Take note that two different recursive calls are made, with
    different order of arguments.
    """
    if height >= 1:
        move_tower(height - 1, from_pole, with_pole, to_pole)
        move_disk(height, from_pole, to_pole)
        move_tower(height - 1, with_pole, to_pole, from_pole)


def move_disk(from_pole: str, to_pole: str):
    """Print out message."""
    print(f"Moving disk from {from_pole} to {to_pole}")


if __name__ == "__main__":
    move_tower(3, "A", "B", "C")
