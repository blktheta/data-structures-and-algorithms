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
"""


def move_tower(height, from_pole, to_pole, with_pole):
    if height >= 1:
        move_tower(height - 1, from_pole, with_pole, to_pole)
        move_disk(from_pole, to_pole)
        move_tower(height - 1, with_pole, to_pole, from_pole)


def move_disk(from_pole, to_pole):
    print(f"Moving disk from {from_pole} to {to_pole}")


if __name__ == "__main__":
    move_tower(3, "A", "B", "C")
