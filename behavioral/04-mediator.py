from abc import ABC, abstractmethod
from typing import Self


class Judge(ABC):
    @abstractmethod
    def notify(self: Self) -> None:
        pass


class Character:
    def __init__(self) -> None:
        self.judge = None


class BattleJudge(Judge):
    def __init__(
        self: Self, character_one: Character, character_two: Character
    ) -> None:
        self.character_one = character_one
        self.character_two = character_two
        character_one.judge = self
        character_two.judge = self

    def notify(self: Self, attack: str) -> None:
        if attack == "Meele":
            self.character_one.block()

        if attack == "Magic":
            self.character_two.not_block()
            print("Mage win!")


class MageCharacter(Character):
    def magic_attack(self: Self):
        self.judge.notify("Magic")

    def block(self: Self):
        print("Mage blocked")


class WarriorCharacter(Character):
    def melee_attack(self: Self):
        self.judge.notify("Meele")

    def not_block(self: Self):
        print("Warrior did not blocked")


if __name__ == "__main__":
    warrior = WarriorCharacter()
    mage = MageCharacter()

    judge = BattleJudge(mage, warrior)

    warrior.melee_attack()
    mage.magic_attack()
