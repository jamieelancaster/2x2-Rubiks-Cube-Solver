import copy

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

    def U(self, n_turns):
        cube = copy.deepcopy(self.cube)

        for _ in range(n_turns):
            # rotate U face
            cube[1] = [elem for row in zip(*cube[1][::-1]) for elem in row]

            # rotate edges
            cube[2][0:2] = list(self.cube[6])[0:2]
            cube[3][0:2] = list(self.cube[2])[0:2]
            cube[5][0:2] = list(self.cube[3])[0:2]
            cube[6][0:2] = list(self.cube[5])[0:2]

            self.cube = copy.deepcopy(cube)
        return cube.copy()

    def L(self, n_turns):
        cube = copy.deepcopy(self.cube)

        for _ in range(n_turns):
            # rotate L face
            cube[2] = [elem for row in zip(*cube[2][::-1]) for elem in row]

            # rotate edges
            cube[1][0], cube[1][3] = self.cube[3][1], self.cube[3][2]
            cube[3][1], cube[3][2] = self.cube[4][3], self.cube[4][0]
            cube[4][0], cube[4][3] = self.cube[6][0], self.cube[6][3]
            cube[6][0], cube[6][3] = self.cube[1][0], self.cube[1][3]

            self.cube = copy.deepcopy(cube)
        return cube.copy()