from .cell import Cell
from .enum import Direction


class Grid:
    width: int
    height: int
    __cells: list[Cell]

    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.__cells = [Cell(col, row) for row in range(height) for col in range(width)]

    def GetCells(self) -> list[Cell]:
        return self.__cells

    def GetCell(self, x: int, y: int) -> Cell:
        idx = self.width * y + x
        return self.__cells[idx]

    def GetNeighbors(self, cell: Cell) -> list[tuple[Direction, Cell]]:
        neighbors: list[tuple[Direction, Cell]] = []

        for dir in Direction:
            dx, dy = cell.x + dir.value[0], cell.y + dir.value[1]

            if 0 <= dx < self.width and 0 <= dy < self.height:
                neighbor = self.GetCell(dx, dy)
                if not neighbor.IsVisited():
                    neighbors.append((dir, neighbor))

        return neighbors
