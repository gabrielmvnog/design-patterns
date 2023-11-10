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


class Sword(ABC):
    @abstractmethod
    def attack(self: Self):
        pass


class ElfSword(ABC):
    def attack(self: Self):
        print("Attacked with elf shield!")


class DwarfSword(ABC):
    def attack(self: Self):
        print("Attacked with dwarf shield!")


class Blacksmith(ABC):
    @abstractmethod
    def sell_shield(self: Self) -> Shield:
        pass

    @abstractmethod
    def sell_sword(self: Self) -> Shield:
        pass


class ElfBlacksmith(Blacksmith):
    def sell_shield(self: Self) -> Shield:
        return ElfShield()

    def sell_sword(self: Self) -> Shield:
        return ElfSword()


class DwarfBlacksmith(Blacksmith):
    def sell_shield(self: Self) -> Shield:
        return DwarfShield()

    def sell_sword(self: Self) -> Sword:
        return DwarfSword()


def buy_and_test(blacksmith: Blacksmith):
    shield: Shield = blacksmith.sell_shield()
    sword: Sword = blacksmith.sell_sword()

    shield.block()
    sword.attack()


if __name__ == "__main__":
    buy_and_test(ElfBlacksmith())

    print("---")

    buy_and_test(DwarfBlacksmith())
