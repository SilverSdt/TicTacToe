# <========== Import ==========>

from __future__ import annotations
from typing import Final
from math import ceil
from itertools import chain

# <========== Class ==========>

class TicTacToe:

    # <----- Static Variables ----->

    __MARKS: Final[list[str]] = ["X", "O"]

    # <----- Constructor ----->

    def __init__(self: TicTacToe, first_player: int = 0) -> None:
        if 0 > first_player or first_player > 1: raise Exception("the first player must be 0 (player 1) or 1 (player 2)")

        self.__grid: list[list[str]] =  [[" "]*3 for i in range(3)]
        self.__current_player: int = first_player

    @property
    def current_player(self: TicTacToe) -> int: return self.__current_player

    def __str__(self: TicTacToe) -> str:
        res: str = ""
        for line in self.__grid:
            res += f"{line.__str__().replace(',','')}\n"
        return res

    def __next_player(self: TicTacToe) -> None:
        self.__current_player = (self.__current_player + 1) % 2

    def __is_valid_target(self: TicTacToe, target: int) -> bool:
        return self.__grid[ceil(target / 3) - 1][target % 3 - 1] not in TicTacToe.__MARKS

    def set_target(self: TicTacToe, target: int) -> bool:
        if target < 1 and target > 9: raise Exception("the target must be between 1 and 9 inclusive")
        if not self.__is_valid_target(target): return False
        else:
            self.__grid[ceil(target / 3) - 1][target % 3 - 1] = TicTacToe.__MARKS[self.__current_player]
            if  not self.is_player_win(): self.__next_player()
            return True

    def is_full(self: TicTacToe) -> bool:
        return not any(" " in case for case in list(chain.from_iterable(self.__grid)))

    def is_player_win(self: TicTacToe) -> bool:
        # Check lines
        for row in self.__grid:
            if row[0] == row[1] == row[2] != " ":
                return True

        # Check column
        for col in range(3):
            if self.__grid[0][col] == self.__grid[1][col] == self.__grid[2][col] != " ":
                return True

        # Check diagonals
        if self.__grid[0][0] == self.__grid[1][1] == self.__grid[2][2] != " ":
            return True
        if self.__grid[0][2] == self.__grid[1][1] == self.__grid[2][0] != " ":
            return True

        return False
    