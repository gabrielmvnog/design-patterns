from abc import ABC, abstractmethod
from typing import Self


class Character(ABC):
    def ultimate(self: Self) -> None:
        print("This is my ULTIMATE")
        self.attack_one()
        self.attack_two()

    @abstractmethod
    def attack_one(self: Self):
        pass

    @abstractmethod
    def attack_two(self: Self):
        pass


class Mage(Character):
    def attack_one(self: Self):
        print("Mage attack one!")

    def attack_two(self: Self):
        print("Mage attack two!")


class Warrior(Character):
    def attack_one(self: Self):
        print("Warrior attack one!")

    def attack_two(self: Self):
        print("Warrior attack two!")


if __name__ == "__main__":
    mage = Mage()
    mage.ultimate()

    print(" --- ")

    warrior = Warrior()
    warrior.ultimate()
