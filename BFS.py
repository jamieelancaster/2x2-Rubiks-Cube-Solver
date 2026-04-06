from cube import Cube
from copy import deepcopy
from collections import deque

def apply_moves(cube):
    moves = []
    for i in range(1, 4):
        move = [("U", "L", "B", "D", "R", "F"), ("U2", "L2", "B2", "D2", "R2", "F2"), ("U'", "L'", "B'", "D'", "R'", "F'")]
        moves.append((move[i-1][0], cube_class.U(i, deepcopy(cube))))
        moves.append((move[i-1][1], cube_class.L(i, deepcopy(cube))))
        moves.append((move[i-1][2], cube_class.B(i, deepcopy(cube))))
        moves.append((move[i-1][3], cube_class.D(i, deepcopy(cube))))
        moves.append((move[i-1][4], cube_class.R(i, deepcopy(cube))))
        moves.append((move[i-1][5], cube_class.F(i, deepcopy(cube))))
    return moves


class Node:
    def __init__(self, state, depth, move):
        self.s = state
        self.d = depth
        self.m = move


def bfs():
    initial_state = {1: ['Y', 'Y', 'Y', 'Y'], 2: ['R', 'R', 'R', 'R'], 3: ['B', 'B', 'B', 'B'], 4: ['W', 'W', 'W', 'W'], 5: ['O', 'O', 'O', 'O'], 6: ['G', 'G', 'G', 'G']}
    root_node = deque([Node(initial_state, 0, "root")])
    visited = set()
    table = {}
    while root_node:
        node = root_node.popleft()
        print(f"Depth: {node.d}, Queue Size: {len(root_node)}")
        state_str = cube_class.to_string(node.s)
        if state_str in visited:
            continue
        visited.add(state_str)

        # apply all moves
        moves = apply_moves(node.s)

        for move, cube in moves:
            inverse = {
                "U":"U'", "U'":"U", "U2":"U2",
                "L": "L'", "L'": "L", "L2": "L2",
                "B": "B'", "B'": "B", "B2": "B2",
                "D": "D'", "D'": "D", "D2": "D2",
                "R": "R'", "R'": "R", "R2": "R2",
                "F": "F'", "F'": "F", "F2": "F2",
            }
            if move != inverse.get(node.m):
                new_state_str = cube_class.to_string(cube)

                root_node.append(Node(cube, node.d+1, move))

                if new_state_str not in table:
                    table[new_state_str] = node.d+1
    return table


cube_class = Cube()
db = bfs()
print(db)