from ..grid import Grid
from abc import abstractmethod


class MazeRenderer:
    @abstractmethod
    def Render(self, grid: Grid) -> None:
        pass
