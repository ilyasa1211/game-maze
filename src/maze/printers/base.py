from ..grid import Grid
from abc import abstractmethod


class MazePrinter:
    @abstractmethod
    def Print(self, grid: Grid) -> None:
        pass
