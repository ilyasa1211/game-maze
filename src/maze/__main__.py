# src/maze/__main__.py
from .renderer import StdoutRenderer, MazeRenderer
from .main import GenerateMaze


def main():
    maze = GenerateMaze(20, 10)

    renderer: set[MazeRenderer] = {
        StdoutRenderer(),
    }

    for r in renderer:
        r.Render(maze)


if __name__ == "__main__":
    main()
