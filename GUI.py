import tkinter as tk
from cube import *
import time

cube_class = Cube()


root = tk.Tk()
root.title("Cube")

canvas = tk.Canvas(root, width=400, height=300)
canvas.pack()


COLOR_MAP = {
    "Y": "yellow",
    "R": "red",
    "B": "blue",
    "W": "white",
    "O": "orange",
    "G": "green"
}

def draw_face(face, start_x, start_y, size):
    size /= 2
    cube_face = cube_class.cube[face].copy()
    label = ["1", "2", "3", "4"]
    if face <4:
        label = label[-(face-1):] + label[:-(face-1)]
        cube_face = cube_face[-(face-1):] + cube_face[:-(face-1)]
    else:
        label = label[-(face - 4):] + label[:-(face - 4)]
        label = label[::-1]
        cube_face = cube_face[(face - 4):] + cube_face[:(face - 4)]
        cube_face = cube_face[::-1]
    for i in range(4):
        color = COLOR_MAP[cube_face[i]]
        x1 = start_x + (1 if i==1 or i==2 else 0)*size
        y1 = start_y + (1 if i>1 else 0)*size
        x2 = x1 + size
        y2 = y1 + size

        canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")
        canvas.create_text(x1+size/2, y1+size/2, text=label[i])


def draw_cube():
    canvas.delete("all")
    size = 60

    draw_face(1, size, size, size)
    draw_face(2, 0, size, size)
    draw_face(3, size, 0, size)
    draw_face(4, size, size*3, size)
    draw_face(5, size*2, size, size)
    draw_face(6, size, size*2, size)

def U():
    cube_class.U(1)
    print(cube_class.cube)
    draw_cube()
    root.update()

def L():
    cube_class.L(1)
    print(cube_class.cube)
    draw_cube()
    root.update()

frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, text="U", command=U)
button.grid(column=0, row=0)
button = tk.Button(frame, text="L", command=L)
button.grid(column=1, row=0)



draw_cube()
root.mainloop()