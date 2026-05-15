

PERM_MASK = 0b111      # lower 3 bits
ORI_MASK = 0b11000     # upper 2 bits


def get_perm(cubie):
    return cubie & PERM_MASK


def get_ori(cubie):
    return cubie >> 3


def set_perm(cubie, perm):
    return (cubie & ORI_MASK) | (perm & 0b111)


def set_ori(cubie, ori):
    return (cubie & PERM_MASK) | ((ori % 3) << 3)


def add_ori(cubie, delta):
    ori = ((cubie >> 3) + delta) % 3
    return (cubie & PERM_MASK) | (ori << 3)

class Cube:
    def __init__(self):
        # solved state:
        # permutation = index
        # orientation = 0
        self.cubies = list(range(8))

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

        cubies = self.orient_cubies(
            cubies,
            orientation_value,
            clockwise
        )

        cubies = self.perm_cubies(
            cubies,
            clockwise
        )

        return cubies

    @staticmethod
    def perm_cubies(cubies, clockwise):

        if clockwise:
            return cubies[-1:] + cubies[:-1]

        return cubies[1:] + cubies[:1]


    @staticmethod
    def orient_cubies(cubies, change_orientation, clockwise):

        if change_orientation == 0:
            pattern = [0, 0, 0, 0]

        elif change_orientation == 1:
            pattern = [1, 2, 1, 2]

        else:
            pattern = [2, 1, 2, 1]

        if not clockwise:
            pattern = pattern[::-1]

        return [
            add_ori(cubies[i], pattern[i])
            for i in range(4)
        ]


    @staticmethod
    def orientation_check(cubies):

        return (
            sum(get_ori(c) for c in cubies)
            % 3
            == 0
        )

    def apply_move(self, move, cube_list):

        move_indices = self.MOVES[move][0]

        index_map = {
            idx: i
            for i, idx in enumerate(move_indices)
        }

        selected = [
            cube_list[i]
            for i in move_indices
        ]

        selected = self.move_cubies(
            selected,
            self.MOVES[move][1][1],
            self.MOVES[move][1][0]
        )

        temp = []

        for i in range(8):

            if i in index_map:
                temp.append(
                    selected[index_map[i]]
                )

            else:
                temp.append(
                    cube_list[i]
                )

        return temp

    def to_sticker_representation(self, cube_list):

        sticker_cube = [
            'W', 'W', 'W', 'W',
            'Y', 'Y', 'Y', 'Y',
            'O', 'O', 'O', 'O',
            'R', 'R', 'R', 'R',
            'B', 'B', 'B', 'B',
            'G', 'G', 'G', 'G'
        ]

        for i in range(8):

            cubie = cube_list[i]

            perm = get_perm(cubie)
            ori = get_ori(cubie)

            stickers = self.COLOR_MAP[perm]

            if ori == 1:
                stickers = (
                        stickers[-1:]
                        + stickers[:-1]
                )

            elif ori == 2:
                stickers = (
                        stickers[1:]
                        + stickers[:1]
                )

            positions = self.PERMUTATION_MAP[i]

            for j in range(3):
                sticker_cube[
                    positions[j]
                ] = stickers[j]

        return sticker_cube

    def state_to_face(self, state):

        state = self.to_sticker_representation(
            state
        )

        return {
            1: list(state[0:4]),
            2: list(state[8:12]),
            3: list(state[20:24]),
            4: list(state[4:8]),
            5: list(state[12:16]),
            6: list(state[16:20]),
        }


cube = Cube()


