from abc import ABC, abstractmethod
from typing import Self


class Equipament(ABC):
    @abstractmethod
    def equip(self: Self):
        pass


class Helmet(Equipament):
    def equip(self: Self):
        print("You now use a helmet")


class Shield(Equipament):
    def equip(self: Self):
        print("You now use a shield")


class Character:
    def __init__(self: Self, equipament: Equipament) -> None:
        self.equipament = equipament

    def equip_equipament(self: Self) -> None:
        self.equipament.equip()


if __name__ == "__main__":
    character = Character(Shield())

    character.equip_equipament()

    character.equipament = Helmet()

    character.equip_equipament()
