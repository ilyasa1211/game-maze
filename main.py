import random
from enum import Enum, IntEnum


class Wall(IntEnum):
    LEFT = 0
    TOP = 1
    RIGHT = 2
    BOTTOM = 3

    @staticmethod
    def FromDirection(dir: Direction) -> Wall:
        return Wall[dir.name]

    @staticmethod
    def Opposite(wall: Wall) -> Wall:
        return Wall((wall.value + 2) % 4)


class Direction(Enum):
    LEFT = (-1, 0)
    TOP = (0, -1)
    RIGHT = (1, 0)
    BOTTOM = (0, 1)


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


class Cell:
    x: int
    y: int
    walls: list[bool]
    __visited: bool = False

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.walls = [True] * 4

    def GetNeighbors(self, grid: Grid) -> list[tuple[Direction, Cell]]:
        neighbors: list[tuple[Direction, Cell]] = []

        for dir in Direction:
            dx, dy = self.x + dir.value[0], self.y + dir.value[1]

            if 0 <= dx < grid.width and 0 <= dy < grid.height:
                neighbor = grid.GetCell(dx, dy)
                if not neighbor.__visited:
                    neighbors.append((dir, neighbor))

        return neighbors

    def RemoveWall(self, wall: Wall) -> None:
        self.walls[wall.value] = False

    def MarkVisited(self) -> None:
        self.__visited = True


class MazePrinter:
    @staticmethod
    def Print(grid: Grid) -> None:
        raise NotImplementedError()


class StdoutMazePrinter(MazePrinter):
    @staticmethod
    def Print(grid: Grid) -> None:
        print("_" * grid.width * 2)

        for r in range(grid.height):
            text = "|"
            for c in range(grid.width):
                cell = grid.GetCell(c, r)
                text += "_" if cell.walls[Wall.BOTTOM] else " "
                text += "|" if cell.walls[Wall.RIGHT] else " "
            print(text)


def main():
    grid = Grid(10, 10)

    cell = random.choice(grid.GetCells())
    cell.MarkVisited()

    stack: list[Cell] = []
    stack.append(cell)

    while len(stack) > 0:
        cell = stack[-1]
        neighbors = cell.GetNeighbors(grid)

        if len(neighbors) > 0:
            direction, neighbor = random.choice(neighbors)

            cell.RemoveWall(Wall.FromDirection(direction))
            neighbor.RemoveWall(Wall.Opposite(Wall.FromDirection(direction)))

            neighbor.MarkVisited()
            stack.append(neighbor)
        else:
            stack.pop()

    StdoutMazePrinter.Print(grid)


if __name__ == "__main__":
    main()
