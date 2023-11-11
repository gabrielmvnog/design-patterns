from datetime import datetime
from random import random
from typing import List, Self


class Character:
    def __init__(self) -> None:
        self.level = 0

    def level_up(self: Self) -> int:
        self.level += 1


class Game:
    def __init__(self: Self, character: Character) -> None:
        self.saves: List = []
        self.character = character

    def save(self: Self) -> None:
        return self.saves.append(
            {"character_level": self.character.level, "datetime": datetime.utcnow()}
        )

    def show_all_saves(self: Self) -> None:
        for save_ in self.saves:
            print(save_)


if __name__ == "__main__":
    mage = Character()

    game = Game(mage)

    mage.level_up()
    game.save()

    mage.level_up()
    game.save()

    mage.level_up()
    game.save()
    
    game.show_all_saves()
