import asyncio
import numpy as np
from datetime import datetime, timedelta
import random


class EndOfQuest(Exception):
    ...


class FoundTheExit(Exception):
    ...


class Environment:
    DIRECTIONS = "NESW"

    def __init__(self, maze):
        self.cells = maze
        self.bot_position = (0, 0)
        self.bot_direction = "E"

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


class Quest:
    def __init__(self, reader, writer):
        self.env = Environment(
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
            # np.array([[2, 0, -1], [0, 0, 0]])
        )

        self.reader = reader
        self.writer = writer
        self.quest = self.name = self.color = None
        self.todo = [
            self.welcome,
            self.questions,
            self.maze,
            self.end,
        ]

    async def act(self):
        if not self.todo:
            self.writer.write("End of quest!")
            raise EndOfQuest
        quest = self.todo.pop(0)
        print("At", quest.__name__)
        await quest()

    async def welcome(self):
        await self.write("Stop!")
        await asyncio.sleep(0.2)
        await self.write(
            "Who would cross the Bridge of Death must answer me these questions three,"
        )
        await asyncio.sleep(0.2)
        await self.write("ere the other side he see.")
        await asyncio.sleep(0.2)

    async def maze(self):
        for line in [
            "Welcome to The Maze.",
            "Instructions are simple:",
            "- `is clear forward?` tells if there's a wall in front of you.",
            "- `move forward` moves you one cell forward.",
            "- `turn left` turns left.",
            "- `turn right` turns right.",
            "",
            "Find the exit.",
        ]:
            await self.write(line)
            await asyncio.sleep(random.random())
        while True:
            action = await self.read()
            if action == "is clear forward?":
                if self.env.is_clear_forward():
                    await self.write("It's clear.")
                else:
                    await self.write("There's a wall.")
            elif action == "turn left":
                self.env.turn_left()
            elif action == "turn right":
                self.env.turn_right()
            elif action == "__debug__":
                await self.write(repr(self.env.cells))
            elif action == "move forward":
                try:
                    self.env.move_forward()
                except ValueError:
                    await self.write("I can't move forward: there's a wall ☹")
                except FoundTheExit:
                    await self.write(
                        f"Congratulations!! {self.name} you found the white rabbit!!"
                    )
                    raise EndOfQuest
            else:
                await self.write("¿Qué?")

    async def end(self):
        await self.write("The end.")
        raise EndOfQuest

    async def write(self, message):
        self.writer.write(message.encode("UTF-8"))
        self.writer.write(b"\n")
        await self.writer.drain()

    async def read(self):
        data = await self.reader.readline()
        if not data:
            raise EndOfQuest
        try:
            message = data.decode("UTF-8")
        except UnicodeError:
            self.write("UTF-8 or GTFO.")
        print(f"Received {message!r}")
        return message.strip()

    async def questions(self):
        while not self.quest:
            await self.write("What is your quest?")
            self.quest = await self.read()
        while not self.name:
            await self.write("What is your name?")
            self.name = await self.read()
        while not self.color:
            await self.write("What is your favorite color?")
            self.color = await self.read()
        await self.write("Right. Off you go.")


async def quest(reader, writer):
    start_at = datetime.now()
    deadline = start_at + timedelta(seconds=30)
    q = Quest(reader, writer)
    while True:
        try:
            await q.act()
        except EndOfQuest:
            break
        if datetime.now() > deadline:
            writer.write(b"Timeout.")
            break
    writer.write(b"Bye.")
    await writer.drain()
    writer.close()


async def amain():
    server = await asyncio.start_server(quest, host="0.0.0.0", port=1975)
    addr = server.sockets[0].getsockname()
    print(f"Serving on {addr}")
    async with server:
        await server.serve_forever()


asyncio.run(amain())
