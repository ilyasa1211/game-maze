from nicegui import ui
from nicegui.element import Element
from maze import GenerateMaze
from maze.enum import Wall
from pathlib import Path


class MazeGame:
    __canvas: Element
    __width: int
    __height: int

    def __init__(self):
        self.__width = 25
        self.__height = 15
        with ui.column().classes("w-full items-center"):
            ui.number(
                label="Width",
                on_change=lambda e: self.set_width(int(e.value)),
                value=self.__width,
                validation={"Must above 0": lambda value: int(value) > 0},
            )
            ui.number(
                label="Height",
                on_change=lambda e: self.set_height(int(e.value)),
                value=self.__height,
                validation={"Must above 0": lambda value: int(value) > 0},
            )

            ui.button("Generate Maze", on_click=self.handle_click)
            self.__canvas = (
                ui.element("canvas")
                .props("id=scratchpad")
                .style("border: 1px solid black;")
            )

    def set_width(self, value: int) -> None:
        self.__width = value

    def set_height(self, value: int) -> None:
        self.__height = value

    async def handle_click(self):
        width, height = self.__width, self.__height

        if width < 1:
            ui.notify("Enter a valid width")
            return

        if height < 1:
            ui.notify("Enter a valid height")
            return

        cell_width = 20
        cell_height = 20
        maze = GenerateMaze(width, height)

        wall: str = "w"
        passage: str = "c"
        actual_width = (maze.width * 2) + 1
        actual_height = maze.height * 2 + 1
        data: list[str] = [wall] * (actual_width * actual_height)

        for r in range(maze.height):
            for c in range(maze.width):
                cell = maze.GetCell(c, r)
                x = c * 2 + 1
                y = r * 2 + 1
                i = y * actual_width + x

                data[i] = passage
                data[i + 1] = wall if cell.walls[Wall.RIGHT] else passage
                data[i + actual_width] = wall if cell.walls[Wall.BOTTOM] else passage

        self.__canvas.props(
            f"data-cell-width={cell_width} data-cell-height={cell_height} data-width={width} data-height={height} data-data={''.join(data)}"
        )

        await self.draw_maze()

    async def draw_maze(self):
        current_dir = Path(__file__).parent
        js_code = (current_dir / "script.js").read_text()
        await ui.run_javascript(js_code)


def main():
    # Start the app
    MazeGame()

    ui.run(host="0.0.0.0", port=8080, reload=False, show=False)


if __name__ == "__main__":
    main()
