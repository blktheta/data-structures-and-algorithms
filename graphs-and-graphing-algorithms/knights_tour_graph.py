from .graph import Graph


def knight_graph(board_size: int) -> Graph:
    kt_graph = Graph()
    for row in range(board_size):
        for col in range(board_size):
            node_id = (row * board_size) + col
            new_positions = gen_legal_moves(row, col, board_size)
            for row2, col2 in new_positions:
                other_node_id = row2 * board_size + col2
                kt_graph.add_edge(node_id, other_node_id)
    return kt_graph


def gen_legal_moves(row: int, col: int, board_size: int) -> list[tuple]:
    new_moves = []
    move_offsets = [
        (-1, -2),   # left-down-down
        (-1, 2),    # left-up-up
        (-2, -1),   # left-left-down
        (-2, 1),    # left-left-up
        (1, -2),    # right-down-down
        (1, 2),     # righ-up-up
        (2, -1),    # right-right-down
        (2, 1),     # right-right-up
    ]
    for r_off, c_off in move_offsets:
        if (0 <= row + r_off < board_size) and (0 <= col + c_off < board_size):
            new_moves.append((row + r_off), col + c_off))
    return new_moves
