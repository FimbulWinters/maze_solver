import random
import time
from cell import Cell


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win, seed=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._exit = None
        self._entrance = None
        self._create_cells()
        self._break_entrance_exit()
        if seed:
            random.seed(seed)
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(self._num_cols):
            col = []
            for j in range(self._num_rows):
                col.append(Cell(self._win))
            self._cells.append(col)

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if not self._win:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._entrance = self._cells[0][0]
        self._cells[self._num_cols-1][self._num_rows-1].has_bottom_wall = False
        self._draw_cell(self._num_cols-1, self._num_rows-1)
        self._exit = self._cells[self._num_cols-1][self._num_rows-1]

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            # check cell to the left
            if i > 0 and not self._cells[i-1][j].visited:
                to_visit.append((i-1, j))
            #  cell to the right
            if i < self._num_cols - 1 and not self._cells[i+1][j].visited:
                to_visit.append((i+1, j))
            # cell above:
            if j > 0 and not self._cells[i][j-1].visited:
                to_visit.append((i, j-1))
            # cell below:
            if j < self._num_rows-1 and not self._cells[i][j+1].visited:
                to_visit.append((i, j+1))

            #  if there are no possible ways to go from this cell because theyve ben visited and/or at an edge
            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return

            #  where to go now?
            direction = random.randrange(len(to_visit))
            next_cell = to_visit[direction]

            # identifiy where the next cells is in relation to the current cell:
            # checking to the right. next_cell[0] refers to the i val in the stored tuple
            if next_cell[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            # check left
            if next_cell[0] == i-1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            # check above:
            if next_cell[1] == j - 1:
                self._cells[i][j-1].has_bottom_wall = False
                self._cells[i][j].has_top_wall = False
            # check below:
            if next_cell[1] == j + 1:
                self._cells[i][j+1].has_top_wall = False
                self._cells[i][j].has_bottom_wall = False
            #  moving swiftly on
            self._break_walls_r(next_cell[0], next_cell[1])

    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        current_cell = self._cells[i][j]
        current_cell.visited = True

        # check if its exit:
        if current_cell == self._exit:
            return True

        # check current cells walls for possible directions:
        possible_directions = []
        # left
        if not current_cell.has_left_wall:
            possible_directions.append((i-1, j))
        # right
        if not current_cell.has_right_wall:
            possible_directions.append((i+1, j))
        # up
        if not current_cell.has_top_wall and current_cell != self._entrance:
            possible_directions.append((i, j-1))
        if not current_cell.has_bottom_wall and current_cell != self._exit:
            possible_directions.append((i, j+1))

        for direction in possible_directions:
            next_cell = self._cells[direction[0]][direction[1]]
            if not next_cell.visited:
                current_cell.draw_move(next_cell)
                success = self._solve_r(direction[0], direction[1])
                if success:
                    return True
                else:
                    current_cell.draw_move(next_cell, True)

        return False
