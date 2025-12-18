# src/maze/__main__.py
import random
from .grid import Grid
from .cell import Cell
from .enum import Wall
from .printers.stdout import StdoutMazePrinter


def main():
    grid = Grid(20, 10)

    cell = random.choice(grid.GetCells())
    cell.MarkAsVisited()

    stack: list[Cell] = []
    stack.append(cell)

    while len(stack) > 0:
        cell = stack[-1]
        neighbors = grid.GetNeighbors(cell)

        if len(neighbors) > 0:
            direction, neighbor = random.choice(neighbors)

            cell.RemoveWall(Wall.FromDirection(direction))
            neighbor.RemoveWall(Wall.Opposite(Wall.FromDirection(direction)))

            neighbor.MarkAsVisited()
            stack.append(neighbor)
        else:
            stack.pop()

    printer = StdoutMazePrinter()
    printer.Print(grid)


if __name__ == "__main__":
    main()
