import copy
import random

class Cube:
    def __init__(self):
        self.cube = {
            1: ["Y"]*4,
            2: ["R"]*4,
            3: ["B"]*4,
            4: ["W"]*4,
            5: ["O"]*4,
            6: ["G"]*4
        }

    def U(self, n_turns, inner_cube):
        cube_copy = copy.deepcopy(inner_cube)
        for _ in range(n_turns):
            temp_copy = copy.deepcopy(cube_copy)
            # rotate U face
            cube_copy[1] = temp_copy[1][-1:] + temp_copy[1][:-1]

            # rotate edges
            cube_copy[2][0], cube_copy[2][1] = temp_copy[6][0], temp_copy[6][1]
            cube_copy[3][1], cube_copy[3][0] = temp_copy[2][0], temp_copy[2][1]
            cube_copy[5][0], cube_copy[5][1] = temp_copy[3][1], temp_copy[3][0]
            cube_copy[6][1], cube_copy[6][0] = temp_copy[5][1], temp_copy[5][0]

        return cube_copy

    def L(self, n_turns, inner_cube):
        cube_copy = copy.deepcopy(inner_cube)
        for _ in range(n_turns):
            temp_copy = copy.deepcopy(cube_copy)
            # rotate L face
            cube_copy[2] = temp_copy[2][-1:] + temp_copy[2][:-1]

            # rotate edges
            cube_copy[1][0], cube_copy[1][3] = temp_copy[3][3], temp_copy[3][0]
            cube_copy[3][0], cube_copy[3][3] = temp_copy[4][3], temp_copy[4][0]
            cube_copy[4][0], cube_copy[4][3] = temp_copy[6][0], temp_copy[6][3]
            cube_copy[6][0], cube_copy[6][3] = temp_copy[1][0], temp_copy[1][3]

        return cube_copy

    def B(self, n_turns, inner_cube):
        cube_copy = copy.deepcopy(inner_cube)
        for _ in range(n_turns):
            temp_copy = copy.deepcopy(cube_copy)
            # rotate B face
            cube_copy[3] = temp_copy[3][1:] + temp_copy[3][:1]

            # rotate edges
            cube_copy[1][0], cube_copy[1][1] = temp_copy[5][1], temp_copy[5][2]
            cube_copy[2][0], cube_copy[2][3] = temp_copy[1][1], temp_copy[1][0]
            cube_copy[4][3], cube_copy[4][2] = temp_copy[2][0], temp_copy[2][3]
            cube_copy[5][1], cube_copy[5][2] = temp_copy[4][2], temp_copy[4][3]

        return cube_copy

    def D(self, n_turns, inner_cube):
        cube_copy = copy.deepcopy(inner_cube)
        for _ in range(n_turns):
            temp_copy = copy.deepcopy(cube_copy)
            # rotate D face
            cube_copy[4] = temp_copy[4][-1:] + temp_copy[4][:-1]

            # rotate edges
            cube_copy[2][3], cube_copy[2][2] = temp_copy[3][2], temp_copy[3][3]
            cube_copy[6][3], cube_copy[6][2] = temp_copy[2][3], temp_copy[2][2]
            cube_copy[5][3], cube_copy[5][2] = temp_copy[6][3], temp_copy[6][2]
            cube_copy[3][2], cube_copy[3][3] = temp_copy[5][3], temp_copy[5][2]

        return cube_copy

    def R(self, n_turns, inner_cube):
        cube_copy = copy.deepcopy(inner_cube)
        for _ in range(n_turns):
            temp_copy = copy.deepcopy(cube_copy)
            # rotate R face
            cube_copy[5] = temp_copy[5][-1:] + temp_copy[5][:-1]

            # rotate edges
            cube_copy[1][1], cube_copy[1][2] = temp_copy[6][1], temp_copy[6][2]
            cube_copy[3][2], cube_copy[3][1] = temp_copy[1][1], temp_copy[1][2]
            cube_copy[4][1], cube_copy[4][2] = temp_copy[3][2], temp_copy[3][1]
            cube_copy[6][1], cube_copy[6][2] = temp_copy[4][1], temp_copy[4][2]

        return cube_copy

    def F(self, n_turns, inner_cube):
        cube_copy = copy.deepcopy(inner_cube)
        for _ in range(n_turns):
            temp_copy = copy.deepcopy(cube_copy)
            # rotate F face
            cube_copy[6] = temp_copy[6][-1:] + temp_copy[6][:-1]

            # rotate edges
            cube_copy[1][3], cube_copy[1][2] = temp_copy[2][2], temp_copy[2][1]
            cube_copy[2][2], cube_copy[2][1] = temp_copy[4][1], temp_copy[4][0]
            cube_copy[4][0], cube_copy[4][1] = temp_copy[5][3], temp_copy[5][0]
            cube_copy[5][0], cube_copy[5][3] = temp_copy[1][3], temp_copy[1][2]

        return cube_copy

    def scramble(self):
        scramble = ""
        for _ in range(20):
            num = random.randint(1, 6)
            match num:
                case 1:
                    self.cube = self.U(1, self.cube)
                    scramble += "U "
                case 2:
                    self.cube = self.L(1, self.cube)
                    scramble += "L "
                case 3:
                    self.cube = self.B(1, self.cube)
                    scramble += "B "
                case 4:
                    self.cube = self.D(1, self.cube)
                    scramble += "D "
                case 5:
                    self.cube = self.R(1, self.cube)
                    scramble += "R "
                case 6:
                    self.cube = self.F(1, self.cube)
                    scramble += "F "

    @staticmethod
    def to_string(inner_cube):
        cube_string = ""
        for i in range(1, 7):
            cube_string += "".join(inner_cube[i])
        return cube_string

c_class = Cube()
cube = c_class.cube
c_class.to_string(cube)
