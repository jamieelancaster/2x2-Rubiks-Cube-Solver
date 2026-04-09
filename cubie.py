from dataclasses import dataclass

# cubie representation
@dataclass
class Cubie:
    position: int # 0-7
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
            0: (4, 14, 23),
            1: (5, 22, 11),
            2: (6, 10, 19),
            3: (7, 18, 15),
            4: (0, 12, 17),
            5: (1, 16, 9),
            6: (2, 8, 21),
            7: (3, 20, 13)
        }

        # self.REVERSE_COLOR_MAP = {v: k for k, v in self.COLOR_MAP.items()}

        self.MOVES = {
            # ([cubies to select], (orientation value, clockwise?))
            "U": ((0, 1, 2, 3), (0, True)),
            "D": ((4, 5, 6, 7), (0, True)),
            "L": ((0, 3, 4, 7), (1, True)),
            "R": ((2, 1, 6, 5), (1, True)),
            "F": ((3, 2, 5, 4), (2, True)),
            "B": ((1, 0, 7, 6), (2, True)),
            "U'": ((0, 1, 2, 3), (0, False)),
            "D'": ((4, 5, 6, 7), (0, False)),
            "L'": ((0, 3, 4, 7), (1, False)),
            "R'": ((2, 1, 6, 5), (1, False)),
            "F'": ((3, 2, 5, 4), (2, False)),
            "B'": ((1, 0, 7, 6), (2, False)),
        }

    @staticmethod
    def move_cubies(cubies, clockwise, orientation_value):
        # orientation value ∈ [0, 1, 2]
        # 0 = U/U' [0, 0, 0, 0]
        # 1 = L/R/F'/B' [2, 1, 2, 1]
        # 2 = F/B/L'/R' [1, 2, 1, 2]
        if not clockwise:
            # reverse list before shifting right for anticlockwise rotation
            cubies.reverse()

        pos_store = cubies[3].position
        for cubie in cubies:
            # apply orientationD
            match orientation_value:
                case 1:
                    cubie.orientation += 2
                    orientation_value = 2
                case 2:
                    cubie.orientation += 1
                    orientation_value = 1
            if cubie.orientation > 2:
                cubie.orientation -= 3

            # shift perm right
            temp_cubie_pos = cubie.position
            cubie.position = pos_store
            pos_store = temp_cubie_pos

        # undo reverse
        if not clockwise:
            cubies.reverse()

        return cubies


    def apply_move(self, move, cube_list):
        selected_cubies = [cube_list[i] for i in self.MOVES[move][0]]
        selected_cubies = self.move_cubies(selected_cubies, self.MOVES[move][1][1], self.MOVES[move][1][0])
        temp_cubies = []
        j = 0
        for i in range(len(self.cubies)):
            if i in self.MOVES[move][0]:
                temp_cubies.append(selected_cubies[j])
                j += 1
            else:
                temp_cubies.append(cube_list[i])
        return temp_cubies

    def to_sticker_representation(self, cube_list):
        sticker_cube = []

        for i in range(len(cube_list)):
            cubie = cube_list[i]

            stickers = self.COLOR_MAP[cubie.position]

            if cubie.orientation == 1:
                # shift right
                stickers = stickers[-1:] + stickers[-1:]
            if cubie.orientation == 2:
                # shift left
                stickers = stickers[1:] + stickers[1:]

            positions = self.PERMUTATION_MAP[i]
            for j in range(len(positions)):
                sticker_cube[positions[j]] = stickers[j]


cube = Cube()


