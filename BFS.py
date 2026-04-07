from cube import Cube
from collections import deque

cube_class = Cube()

# Indices:
# U: 0–3
# D: 4–7
# L: 8–11
# R: 12–15
# F: 16–19
# B: 20–23


MOVES = []
for m in ["U","R","F"]:
    MOVES.append((m, 1))
    MOVES.append((m, 2))
    MOVES.append((m, 3))


def compose(a, b):
    return [a[b[i]] for i in range(24)]

MOVE_TABLE = {}
for move in ["U", "R", "F"]:
    base = cube_class.MOVES[move]

    m1 = base
    m2 = compose(base, base)
    m3 = compose(m2, base)

    MOVE_TABLE[(move, 1)] = m1
    MOVE_TABLE[(move, 2)] = m2
    MOVE_TABLE[(move, 3)] = m3

COLOR_MAP = {
    "Y": 0,
    "W": 1,
    "R": 2,
    "O": 3,
    "G": 4,
    "B": 5
}

def encode(state):
    x = 0
    for v in state:
        x = (x << 3) | v
    return x


def apply_move(state_bytes, move, turns):
    perm = MOVE_TABLE[(move, turns)]
    return bytes(state_bytes[perm[i]] for i in range(24))

def bfs():
    buffer = []
    buffer_size = 10000

    initial_state = bytes(COLOR_MAP[x] for x in cube_class.INITIAL_STATE)

    queue = deque([(initial_state, 0, "root")])

    # to be replaced
    visited = {initial_state: 0}

    file = open("cube_db.bin", "wb")

    while queue:
        state, depth, prev_move = queue.popleft()
        if len(visited) % 10000 == 0:
            print(
                f"Depth: {depth}, Queue: {len(queue)}, "
                f"Visited: {len(visited)}, "
                f"Completed: {int(100*(len(visited)/3674160))}%"
            )

        for move_name, turns in MOVES:
            # prune same move on face
            if prev_move != "root" and move_name[0] == prev_move[0]:
                continue

            new_state = apply_move(state, move_name, turns)

            if new_state not in visited:
                visited[new_state] = depth + 1

                buffer.append(new_state + bytes([depth + 1]))

                if len(buffer) >= buffer_size:
                    file.writelines(buffer)
                    buffer.clear()

                queue.append((new_state, depth+1, move_name))
    if buffer:
        file.writelines(buffer)
    file.close()
    return visited


db = bfs()


