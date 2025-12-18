from .enum import Wall


class Cell:
    x: int
    y: int
    walls: list[bool]
    __visited: bool = False

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.walls = [True] * 4

    def RemoveWall(self, wall: Wall) -> None:
        self.walls[wall.value] = False

    def MarkAsVisited(self) -> None:
        self.__visited = True

    def IsVisited(self) -> bool:
        return self.__visited
