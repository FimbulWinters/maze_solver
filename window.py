from tkinter import Tk, BOTH, Canvas
from line import Line


class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title = "Maze Solver 1.0"
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(self.root, bg="black", height=height, width=width)
        self.canvas.pack(fill=BOTH, expand=1)
        self.running = False

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
        print("closed...")

    def close(self):
        self.running = False
        self.root

    def draw_line(self, line, colour="white"):
        line.draw(self.canvas, colour)
