from ..grid import Grid
from .base import MazePrinter
from ..enum import Wall


class StdoutMazePrinter(MazePrinter):
    def Print(self, grid: Grid) -> None:
        print(" " + "_" * (grid.width * 2 - 1))

        for r in range(grid.height):
            text = "|"
            for c in range(grid.width):
                cell = grid.GetCell(c, r)
                text += "_" if cell.walls[Wall.BOTTOM] else " "
                text += "|" if cell.walls[Wall.RIGHT] else " "
            print(text)
