import unittest
from maze import Maze
from window import Window


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        cols = 12
        rows = 10
        maze = Maze(10, 10, rows, cols, 800/rows, 600/cols, Window(800, 600))

        self.assertEqual(
            len(maze._cells), cols
        )
        self.assertEqual(len(maze._cells[0]), rows)


if __name__ == "__main__":
    unittest.main()
