import tkinter as tk
from cubie import *

cube = Cube()


root = tk.Tk()
root.title("Cube")

canvas = tk.Canvas(root, width=400, height=300)
canvas.pack()


COLOR_MAP = {
    "W": "white",
    "Y": "yellow",
    "O": "orange",
    "R": "red",
    "B": "blue",
    "G": "green"
}

def draw_face(face, start_x, start_y, size):
    size /= 2
    faces = cube.state_to_face(cube.cubies)
    cube_face = faces[face].copy()
    # label = ["0", "1", "2", "3"]
    if face < 4:
        # label = label[-(face-1):] + label[:-(face-1)]
        cube_face = cube_face[-(face-1):] + cube_face[:-(face-1)]
    if face > 4:
        # label = label[-(face -6):] + label[:-(face -6)]
        cube_face = cube_face[-(face -6):] + cube_face[:-(face -6)]
    for i in range(4):
        color = COLOR_MAP[cube_face[i]]
        x1 = start_x + (1 if i==1 or i==2 else 0)*size
        y1 = start_y + (1 if i>1 else 0)*size
        x2 = x1 + size
        y2 = y1 + size

        canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")
        # canvas.create_text(x1+size/2, y1+size/2, text=i)
    canvas.create_rectangle(start_x, start_y, start_x+size*2, start_y+size*2, outline="black", width=3)


def draw_cube():

    canvas.delete("all")
    size = 60

    draw_face(1, size, size, size)
    draw_face(2, 0, size, size)
    draw_face(3, size, 0, size)
    draw_face(4, size, size*3, size)
    draw_face(5, size*2, size, size)
    draw_face(6, size, size*2, size)

def refresh():
    draw_cube()
    root.update()

def scramble():
    s = cube.scramble()
    refresh()
    print(s)

def move(move):
    cube.cubies = cube.apply_move(move, cube.cubies)
    # print(cube.cubies)
    refresh()

frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, text="U", command=lambda: move("U"))
button.grid(column=0, row=0)
button = tk.Button(frame, text="D", command=lambda: move("D"))
button.grid(column=1, row=0)
button = tk.Button(frame, text="L", command=lambda: move("L"))
button.grid(column=2, row=0)
button = tk.Button(frame, text="R", command=lambda: move("R"))
button.grid(column=3, row=0)
button = tk.Button(frame, text="F", command=lambda: move("F"))
button.grid(column=4, row=0)
button = tk.Button(frame, text="B", command=lambda: move("B"))
button.grid(column=5, row=0)

button = tk.Button(frame, text="U'", command=lambda: move("U'"))
button.grid(column=0, row=1)
button = tk.Button(frame, text="D'", command=lambda: move("D'"))
button.grid(column=1, row=1)
button = tk.Button(frame, text="L'", command=lambda: move("L'"))
button.grid(column=2, row=1)
button = tk.Button(frame, text="R'", command=lambda: move("R'"))
button.grid(column=3, row=1)
button = tk.Button(frame, text="F'", command=lambda: move("F'"))
button.grid(column=4, row=1)
button = tk.Button(frame, text="B'", command=lambda: move("B'"))
button.grid(column=5, row=1)


button = tk.Button(frame, text="scramble", command=scramble)
button.grid(column=0, row=3)



draw_cube()
root.mainloop()