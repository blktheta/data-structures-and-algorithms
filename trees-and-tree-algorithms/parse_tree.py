from stack import Stack
from binary_tree import BinaryTree

import operator


def evaluate(parse_tree: BinaryTree):
    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }

    left_child = parse_tree.left_child
    right_child = parse_tree.right_child

    if left_child and right_child:
        fn = operators[parse_tree.root]
        return fn(evaluate(left_child), evaluate(right_child))
    else:
        return parse_tree.root


def build_parse_tree(fp_expr) -> BinaryTree:
    fp_list = fp_expr.split()
    p_stack = Stack()
    expr_tree = BinaryTree("")
    p_stack.push(expr_tree)
    current_tree = expr_tree

    for i in fp_list:
        if i == "(":
            current_tree.insert_left("")
            p_stack.push(current_tree)
            current_tree = current_tree.left_child
        elif i in ["+", "-", "*", "/"]:
            current_tree.root = i
            current_tree.insert_right("")
            p_stack.push(current_tree)
            current_tree = current_tree.right_child
        elif i.isdigit():
            current_tree.root = int(i)
            parent = p_stack.pop()
            current_tree = parent
        elif i == ")":
            current_tree = p_stack.pop()
        else:
            raise ValueError(f"Unknown operator '{i}'")
    return expr_tree


pt = build_parse_tree("( 3 + ( 4 * 5 ) )")
ptx = build_parse_tree("( ( 10 + 5 ) * 3 )")
print(evaluate(ptx))
