from abc import ABC, abstractmethod
from typing import Self


class Shield(ABC):
    @abstractmethod
    def block(self: Self):
        pass


class ElfShield(ABC):
    def block(self: Self):
        print("Blocked with elf shield!")


class DwarfShield(ABC):
    def block(self: Self):
        print("Blocked with dwarf shield!")


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


def buy_and_test(blacksmith: Blacksmith):
    shield: Shield = blacksmith.sell_shield()

    shield.block()


if __name__ == "__main__":
    buy_and_test(ElfBlacksmith())

    print("---")

    buy_and_test(DwarfBlacksmith())
