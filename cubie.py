from dataclasses import dataclass

# cubie representation
@dataclass
class Cubie:
    position: int # 0-7
    orientation: int # 0-2 1=clockwise, 2=anticlockwise
    # orientation reference = white top, green front

    # clockwise move always shifts selected 4 pieces to the right
    # [0, 1, 2, 3] -> [3, 0, 1, 2]

    # move on U/D doesn't change orientation
    # L/R [2, 1, 2, 1]
    # F/B [1, 2, 1, 2]

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

        self.REVERSE_COLOR_MAP = {v: k for k, v in self.COLOR_MAP.items()}

cube = Cube()
