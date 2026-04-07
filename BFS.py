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
    MOVES.append((m + "'", 3))
    MOVES.append((m+"2", 2))


def apply_moves(state, move, turns):
    move_map = cube_class.MOVES[move]
    for _ in range(turns):
        temp=state[:]
        for idx, target in enumerate(move_map):
            state[idx] = temp[target]
    return state


def bfs():
    buffer = []
    BUFFER_SIZE = 10000

    initial_state = list(cube_class.INITIAL_STATE)

    queue = deque([(initial_state, 0, "root")])
    table = {tuple(initial_state): 0}

    file = open("cube_db.txt", "w")

    while queue:
        state, depth, prev_move = queue.popleft()
        if len(queue) % 10000 == 0:
            print(f"Depth: {depth}, Queue: {len(queue)}, Visited: {len(table)}, Completed: {int(100*(len(table)/3674160))}%")

        for move_name, turns in MOVES:
            # prune same move on face
            if prev_move != "root" and move_name[0] == prev_move[0]:
                continue

            # treat U2 as U(2), U' as U(3)
            base_move = move_name[0]
            new_state = apply_moves(state[:], base_move, turns)

            key= tuple(new_state)

            if key not in table:
                table[key] = depth + 1
                buffer.append(f"{"".join(key)},{depth + 1}\n")

                if len(buffer) >= BUFFER_SIZE:
                    file.writelines(buffer)
                    buffer.clear()
                queue.append((new_state[:], depth+1, move_name))
    if buffer:
        file.writelines(buffer)
    file.close()
    return table


db = bfs()