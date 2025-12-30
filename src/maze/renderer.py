from .grid import Grid
from .enum import Wall
from abc import abstractmethod

class MazeRenderer:
    @abstractmethod
    def Render(self, grid: Grid) -> None:
        pass


class StdoutRenderer(MazeRenderer):
    __horizontal_wall: str
    __vertical_wall: str

    def __init__(self, horizontal_wall: str = "_", vertical_wall: str = "|") -> None:
        super().__init__()
        self.__horizontal_wall = horizontal_wall
        self.__vertical_wall = vertical_wall

    def Render(self, grid: Grid) -> None:
        super().Render(grid)
        print(self.__horizontal_wall * (grid.width * 2 + 1))

        for r in range(grid.height):
            text = self.__vertical_wall
            for c in range(grid.width):
                cell = grid.GetCell(c, r)
                text += self.__horizontal_wall if cell.walls[Wall.BOTTOM] else " "
                text += self.__vertical_wall if cell.walls[Wall.RIGHT] else " "
            print(text)
