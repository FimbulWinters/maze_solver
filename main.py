from cell import Cell
from maze import Maze
from point import Point
from window import Window
from line import Line


def main():
    rows = 12
    cols = 10
    win = Window(800, 600)
    maze = Maze(10, 10, rows, cols, 800/rows, 600/cols, win)
    maze.solve()
    win.wait_for_close()


main()
