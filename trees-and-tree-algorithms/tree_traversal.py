"""
3 Common Tree Traversal Patterns.

1. Preorder
In a preorder traversal, we visit the root node first, then recursively do a
preorder traversal of the left subtree, followed by a recursive preorder
traversal of the right subtree.


2. Inorder
In an inorder traversal, we recursively do an inorder traversal on the left
subtree, visit the root node, and finally do a recursive inorder traversal
of the right subtree.

3. Postorder
In a postorder traversal, we recursively do a postorder traversal of the
left subtree and the right subtree followed by a visit to the root node.

"""
from typing import TypeVar


T = TypeVar("T")


def preorder(tree: T):
    """Implementing preorder traversal for a binary tree."""
    if tree:
        print(tree.key)
        preorder(tree.left_child)
        preorder(tree.right_child)


def postorder(tree: T):
    """Implementing postorder traversal for a binary tree."""
    if tree:
        postorder(tree.left_child)
        postorder(tree.right_child)
        print(tree.key)


def inorder(tree: T):
    """Implementing inorder traversal for a binary tree."""
    if tree:
        inorder(tree.left_child)
        print(tree.key)
        inorder(tree.right_child)
