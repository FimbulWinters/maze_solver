from line import Line
from point import Point


class Cell:
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self.win = win

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        if self.has_left_wall:

            line = Line(Point(x1, y1), Point(x1, y2))
            self.win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self.win.draw_line(line, "black")
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self.win.draw_line(line)
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self.win.draw_line(line, "black")
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self.win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self.win.draw_line(line, "black")
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self.win.draw_line(line)
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self.win.draw_line(line, "black")

    def draw_move(self, to_cell, undo=False):
        colour = "green"
        if undo:
            colour = "red"
        self.win.draw_line(
            Line(self.calc_center(), to_cell.calc_center()), colour)

    def calc_center(self):
        x_center = (self._x1 + self._x2) / 2
        y_center = (self._y2 + self._y1) / 2
        return Point(x_center, y_center)
