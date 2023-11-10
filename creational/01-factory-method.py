from abc import ABC, abstractmethod
from typing import Self


class Shield(ABC):
    @abstractmethod
    def equip(self: Self):
        pass


class ElfShield(ABC):
    def equip(self: Self):
        print("Equiped a elf shield!")


class DwarfShield(ABC):
    def equip(self: Self):
        print("Equiped a dwarf shield!")


class Blacksmith(ABC):
    @abstractmethod
    def sell_shield(self: Self) -> Shield:
        pass


class ElfBlacksmith(Blacksmith):
    def sell_shield(self: Self) -> Shield:
        return ElfShield()


class DwarfBlacksmith(Blacksmith):
    def sell_shield(self: Self) -> Shield:
        return DwarfShield()


def buy_shield(blacksmith: Blacksmith):
    return blacksmith.sell_shield()


if __name__ == "__main__":
    shield: Shield = buy_shield(ElfBlacksmith())
    shield.equip()

    shield: Shield = buy_shield(DwarfBlacksmith())
    shield.equip()
