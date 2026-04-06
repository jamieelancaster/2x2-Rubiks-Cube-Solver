import copy
import random

class Cube:
    def __init__(self):
        self.cube = {
            1: ["Y","Y","Y","Y"],
            2: ["R"]*4,
            3: ["B"]*4,
            4: ["W"]*4,
            5: ["O"]*4,
            6: ["G"]*4
        }

    def U(self, n_turns):
        cube = copy.deepcopy(self.cube)

        for _ in range(n_turns):
            # rotate U face
            cube[1] = cube[1][-1:] + cube[1][:-1]

            # rotate edges
            cube[2][0], cube[2][1] = self.cube[6][0], self.cube[6][1]
            cube[3][1], cube[3][0] = self.cube[2][0], self.cube[2][1]
            cube[5][0], cube[5][1] = self.cube[3][1], self.cube[3][0]
            cube[6][1], cube[6][0] = self.cube[5][1], self.cube[5][0]

            self.cube = copy.deepcopy(cube)

    def L(self, n_turns):
        cube = copy.deepcopy(self.cube)

        for _ in range(n_turns):
            # rotate L face
            cube[2] = cube[2][-1:] + cube[2][:-1]

            # rotate edges
            cube[1][0], cube[1][3] = self.cube[3][3], self.cube[3][0]
            cube[3][0], cube[3][3] = self.cube[4][3], self.cube[4][0]
            cube[4][0], cube[4][3] = self.cube[6][0], self.cube[6][3]
            cube[6][0], cube[6][3] = self.cube[1][0], self.cube[1][3]

            self.cube = copy.deepcopy(cube)

    def B(self, n_turns):
        cube = copy.deepcopy(self.cube)

        for _ in range(n_turns):
            # rotate B face
            cube[3] = cube[3][1:] + cube[3][:1]

            # rotate edges
            cube[1][0], cube[1][1] = self.cube[5][1], self.cube[5][2]
            cube[2][0], cube[2][3] = self.cube[1][1], self.cube[1][0]
            cube[4][3], cube[4][2] = self.cube[2][0], self.cube[2][3]
            cube[5][1], cube[5][2] = self.cube[4][2], self.cube[4][3]

            self.cube = copy.deepcopy(cube)

    def D(self, n_turns):
        cube = copy.deepcopy(self.cube)

        for _ in range(n_turns):
            # rotate D face
            cube[4] = cube[4][-1:] + cube[4][:-1]

            # rotate edges
            cube[2][3], cube[2][2] = self.cube[3][2], self.cube[3][3]
            cube[6][3], cube[6][2] = self.cube[2][3], self.cube[2][2]
            cube[5][3], cube[5][2] = self.cube[6][3], self.cube[6][2]
            cube[3][2], cube[3][3] = self.cube[5][3], self.cube[5][2]

            self.cube = copy.deepcopy(cube)

    def R(self, n_turns):
        cube = copy.deepcopy(self.cube)

        for _ in range(n_turns):
            # rotate R face
            cube[5] = cube[5][-1:] + cube[5][:-1]

            # rotate edges
            cube[1][1], cube[1][2] = self.cube[6][1], self.cube[6][2]
            cube[3][2], cube[3][1] = self.cube[1][1], self.cube[1][2]
            cube[4][1], cube[4][2] = self.cube[3][2], self.cube[3][1]
            cube[6][1], cube[6][2] = self.cube[4][1], self.cube[4][2]

            self.cube = copy.deepcopy(cube)

    def F(self, n_turns):
        cube = copy.deepcopy(self.cube)

        for _ in range(n_turns):
            # rotate F face
            cube[6] = cube[6][-1:] + cube[6][:-1]

            # rotate edges
            cube[1][3], cube[1][2] = self.cube[2][2], self.cube[2][1]
            cube[2][2], cube[2][1] = self.cube[4][1], self.cube[4][0]
            cube[4][0], cube[4][1] = self.cube[5][3], self.cube[5][0]
            cube[5][0], cube[5][3] = self.cube[1][3], self.cube[1][2]

            self.cube = copy.deepcopy(cube)
