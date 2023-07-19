"""
BinaryTree() creates a new instance of a binary tree.
get_root_val() returns the object stored in the current node.
set_root_val(val) stores the object in parameter val in the current node.
get_left_child() returns the binary tree corresponding to the left child of the current node.
get_right_child() returns the binary tree corresponding to the right child of the current node.
insert_left(val) creates a new binary tree and installs it as the left child of the current node.
insert_right(val) creates a new binary tree and installs it as the right child of the current node.
"""
from typing import TypeVar
import operator

T = TypeVar("T")


class BinaryTree:
    def __init__(self, root_obj: T):
        self.key = root_obj
        self.left_child: BinaryTree = None
        self.right_child: BinaryTree = None

    def insert_left(self, new_node: T):
        if self.left_child is None:
            self.left_child = BinaryTree(new_node)
        else:
            new_child = BinaryTree(new_node)
            new_child.left_child = self.left_child
            self.left_child = new_child

    def insert_right(self, new_node: T):
        if self.right_child is None:
            self.right_child = BinaryTree(new_node)
        else:
            new_child = BinaryTree(new_node)
            new_child.right_child = self.right_child
            self.right_child = new_child

    def get_root_val(self) -> T:
        return self.key

    def set_root_val(self, new_obj: T):
        self.key = new_obj

    def get_left_child(self) -> T:
        return self.left_child

    def get_right_child(self) -> T:
        return self.right_child


"""Traversal methods"""


def preorder(tree: T):
    if tree:
        print(tree.key)
        preorder(tree.left_child)
        preorder(tree.right_child)


def postorder(tree: T):
    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }

    result_1 = None
    result_2 = None

    if tree:
        result_1 = postorder(tree.left_child)
        result_2 = postorder(tree.right_child)
        if result_1 and result_2:
            return operators[tree.key](result_1, result_2)
        return tree.key


def print_exp(tree: T):
    result = ""
    if tree:
        result = "(" + print_exp(tree.left_child)
        result = result + str(tree.key)
        result = result + print_exp(tree.right_child) + ")"
    return result


def main():
    btree = BinaryTree("a")
    print(btree.get_root_val())
    print(btree.get_left_child())
    btree.insert_left("b")
    print(btree.get_left_child())
    print(btree.get_left_child().get_root_val())
    btree.insert_right("c")
    print(btree.get_right_child())
    print(btree.get_right_child().get_root_val())
    btree.get_right_child().set_root_val("hello")
    print(btree.get_right_child().get_root_val())


if __name__ == "__main__":
    main()
