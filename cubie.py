from dataclasses import dataclass

# cubie representation
@dataclass
class Cubie:
    id: int # 0-7
    orientation: int # 0-2 1=clockwise, 2=anticlockwise
    # orientation reference = white top, green front

    # clockwise move always shifts selected 4 pieces to the right
    # [0, 1, 2, 3] -> [3, 0, 1, 2]

    # 3 2 1 0
    # 0 3 2 1
    # 1 2 3 0

    # move on U/D doesn't change orientation
    # L/R/F'/B' [2, 1, 2, 1]
    # F/B/L'/R' [1, 2, 1, 2]

class Cube:
    def __init__(self):
        # 8 cubies
        # matrix to define moves
        # func to turn into sticker view for GUI
        # label cubie 1, 2, 3, 4... to describe permutation
        # 0, 1, 2 to describe orientation, 0= white/yellow top, 1= clockwise, 2= anticlockwise
        self.cubies = [Cubie(i, 0) for i in range(8)]

        self.COLOR_MAP = {
            0: "WOB",
            1: "WBR",
            2: "WRG",
            3: "WGO",
            4: "YOG",
            5: "YGR",
            6: "YRB",
            7: "YBO"
        }

        self.PERMUTATION_MAP = {
            0: (0, 8, 21),
            1: (1, 20, 13),
            2: (2, 12, 17),
            3: (3, 16, 9),
            4: (4, 10, 19),
            5: (5, 18, 15),
            6: (6, 14, 23),
            7: (7, 22, 11),
        }

        # self.REVERSE_COLOR_MAP = {v: k for k, v in self.COLOR_MAP.items()}

        self.MOVES = {
            # ([cubies to select], (orientation value, clockwise?))
            "U": ((0, 1, 2, 3), (0, True)),
            "D": ((4, 5, 6, 7), (0, True)),
            "L": ((0, 3, 4, 7), (1, True)),
            "R": ((2, 1, 6, 5), (1, True)),
            "F": ((3, 2, 5, 4), (1, True)),
            "B": ((1, 0, 7, 6), (1, True)),
            "U'": ((0, 1, 2, 3), (0, False)),
            "D'": ((4, 5, 6, 7), (0, False)),
            "L'": ((0, 3, 4, 7), (2, False)),
            "R'": ((2, 1, 6, 5), (2, False)),
            "F'": ((3, 2, 5, 4), (2, False)),
            "B'": ((1, 0, 7, 6), (2, False)),
        }

    def move_cubies(self, cubies, clockwise, orientation_value):
        print(cubies)
        cubies = self.orient_cubies(cubies, orientation_value, clockwise)
        print(cubies)
        cubies = self.perm_cubies(cubies, clockwise)
        print(cubies)
        return cubies

    @staticmethod
    def perm_cubies(cubies, clockwise):
        if clockwise:
            return cubies[-1:] + cubies[:-1]
        else:
            return cubies[1:] + cubies[:1]

    @staticmethod
    def orient_cubies(cubies, change_orientation, clockwise):
        if change_orientation == 0:
            pattern = [0, 0, 0, 0]
        elif change_orientation == 1:
            pattern = [1, 2, 1, 2]
        else:
            pattern = [2,1,2,1]

        # reverse pattern for anticlockwise
        if not clockwise:
            pattern = pattern[::-1]

        for i in range(4):
            cubies[i].orientation = (cubies[i].orientation + pattern[i]) % 3

        return cubies

    @staticmethod
    def orientation_check(cubies):
        return sum(cubie.orientation for cubie in cubies) % 3 == 0

    def apply_move(self, move, cube_list):
        move_indices = self.MOVES[move][0]
        index_map = {idx: i for i, idx in enumerate(move_indices)}

        selected_cubies = [cube_list[i] for i in move_indices]
        selected_cubies = self.move_cubies(
            selected_cubies,
            self.MOVES[move][1][1],
            self.MOVES[move][1][0]
        )

        temp_cubies = []
        for i in range(len(self.cubies)):
            if i in index_map:
                temp_cubies.append(selected_cubies[index_map[i]])
            else:
                temp_cubies.append(cube_list[i])

        return temp_cubies

    def to_sticker_representation(self, cube_list):
        sticker_cube = [
            'W', 'W', 'W', 'W',  # U 0-3
            'Y', 'Y', 'Y', 'Y',  # D 4-7
            'O', 'O', 'O', 'O',  # L 8-11
            'R', 'R', 'R', 'R',  # R 12-15
            'B', 'B', 'B', 'B',  # F 16-19
            'G', 'G', 'G', 'G'  # B 20-23
        ]

        for i in range(len(cube_list)):
            cubie = cube_list[i]

            stickers = self.COLOR_MAP[cubie.id]

            if cubie.orientation == 1:
                # shift right
                stickers = stickers[-1:] + stickers[:-1]
            if cubie.orientation == 2:
                # shift left
                stickers = stickers[1:] + stickers[:1]

            positions = self.PERMUTATION_MAP[i]
            for j in range(len(positions)):
                sticker_cube[positions[j]] = stickers[j]

        return sticker_cube


    def state_to_face(self, state):
        state = self.to_sticker_representation(state)
        return {
            1: list(state[0:4]),
            2: list(state[8:12]),
            3: list(state[20:24]),
            4: list(state[4:8]),
            5: list(state[12:16]),
            6: list(state[16:20]),
        }


cube = Cube()


