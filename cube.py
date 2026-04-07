import random

class Cube:
    def __init__(self):
        self.INITIAL_STATE = (
            'Y', 'Y', 'Y', 'Y',  # U
            'W', 'W', 'W', 'W',  # D
            'R', 'R', 'R', 'R',  # L
            'O', 'O', 'O', 'O',  # R
            'G', 'G', 'G', 'G',  # F
            'B', 'B', 'B', 'B'  # B
        )

        self.COLOR_MAP = {
            "Y": 0,
            "W": 1,
            "R": 2,
            "O": 3,
            "G": 4,
            "B": 5
        }

        self.REVERSE_COLOR_MAP = {v: k for k, v in self.COLOR_MAP.items()}

        self.cube = self.INITIAL_STATE

        self.MOVES = {
            "U": [3,0,1,2, 4,5,6,7, 16,17,10,11, 20,21,14,15, 12,13,18,19, 8,9,22,23],

            "D": [0,1,2,3, 7,4,5,6, 8,9,22,23, 12,13,18,19, 16,17,10,11, 20,21,14,15],

            "L": [22,1,2,21, 16,5,6,19, 11,8,9,10, 12,13,14,15, 0,17,18,3, 20,7,4,23],

            "R": [0,17,18,3, 4,23,20,7, 8,9,10,11, 15,12,13,14, 16,5,6,19, 2,21,22,1],

            "F": [0,1,9,10, 15,12,6,7, 8,4,5,11, 3,13,14,2, 19,16,17,18, 20,21,22,23],

            "B": [13,14,2,3, 4,5,11,8, 1,9,10,0, 12,6,7,15, 16,17,18,19, 23,20,21,22],
        }


    def apply_move(self, move, n):
        for _ in range(n):
            self.cube = tuple(self.cube[i] for i in self.MOVES[move])

    def scramble(self):
        moves = ["U", "D", "L", "R", "F", "B"]
        scramble = ""
        for _ in range(20):
            m = random.choice(moves)
            self.apply_move(m, 1)
            scramble += m + " "
        return scramble

    @staticmethod
    def state_to_face(state):
        return {
            1: list(state[0:4]),
            2: list(state[8:12]),
            3: list(state[20:24]),
            4: list(state[4:8]),
            5: list(state[12:16]),
            6: list(state[16:20]),
        }

    @staticmethod
    def to_string(state):
        return "".join(state)

c_class = Cube()