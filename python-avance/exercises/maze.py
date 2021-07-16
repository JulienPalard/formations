import numpy as np
import matplotlib.pyplot as plt


class Bot:
    def __init__(self, environment):
        self.environment = environment

    def act(self):
        self.environment.turn_left()
        if self.environment.is_clear_forward():
            self.environment.move_forward()
            return
        while True:
            self.environment.turn_right()
            if self.environment.is_clear_forward():
                self.environment.move_forward()
                return


class FoundTheExit(Exception):
    ...


class Environment:
    DIRECTIONS = "NESW"

    def __init__(self, maze):
        self.cells = maze
        self.bot_position = (0, 0)
        self.bot_direction = "N"

    def turn_left(self):
        self.bot_direction = self.DIRECTIONS[
            self.DIRECTIONS.index(self.bot_direction) - 1
        ]

    def turn_right(self):
        self.bot_direction = self.DIRECTIONS[
            self.DIRECTIONS.index(self.bot_direction) - 3
        ]

    def _next_cell(self):
        x, y = self.bot_position
        if self.bot_direction == "N":
            y -= 1
        if self.bot_direction == "S":
            y += 1
        if self.bot_direction == "W":
            x -= 1
        if self.bot_direction == "E":
            x += 1
        return x, y

    def is_clear_forward(self):
        x, y = self._next_cell()
        if x < 0 or x >= self.cells.shape[0]:
            return False
        if y < 0 or y >= self.cells.shape[1]:
            return False
        return self.cells[x, y] == 0 or self.cells[x, y] == -1

    def move_forward(self):
        if not self.is_clear_forward():
            raise ValueError("Can't move forward.")
        self.cells[self.bot_position] = 0
        self.bot_position = self._next_cell()
        if self.cells[self.bot_position] == -1:
            raise FoundTheExit()
        self.cells[self.bot_position] = 2


fig, ax = plt.subplots()


env = Environment(
    np.array(
        [
            [2, 0, 0, 1, 1, 0, 0, 0, 1, 1],
            [0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 0, 1, 0, 0],
            [1, 0, 0, 0, 1, 0, 0, 1, 0, 0],
            [1, 1, 0, 1, 1, 1, 0, 1, 1, 0],
            [0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
            [0, 1, 0, 1, 1, 0, 1, 1, 1, 0],
            [0, 1, 0, 1, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 1, 1, 0, 1, 1],
            [1, 1, 0, 0, 0, 1, 0, 0, -1, 1],
        ]
    )
)
bot = Bot(env)
image = ax.imshow(env.cells)
while True:
    bot.act()
    image.set_data(env.cells)
    plt.pause(0.1)
