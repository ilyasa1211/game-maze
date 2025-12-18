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
