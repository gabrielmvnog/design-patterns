from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Self


@dataclass
class Armour:
    helmet: str = ""
    gauntlets: str = ""
    greaves: str = ""


class Blacksmith(ABC):
    _armour: Armour

    @abstractmethod
    def set_helmet(self: Self):
        pass

    @abstractmethod
    def set_gauntlets(self: Self):
        pass

    @abstractmethod
    def set_greaves(self: Self):
        pass

    def reset(self: Self):
        self._armour = Armour()

    def get_armour(self: Self):
        armour = self._armour
        self.reset()
        return armour


class ElfBlacksmith(Blacksmith):
    def __init__(self) -> None:
        self.reset()

    def set_helmet(self: Self):
        self._armour.helmet = "Elf helmet"

    def set_gauntlets(self: Self):
        self._armour.gauntlets = "Elf gauntlets"

    def set_greaves(self: Self):
        self._armour.helmet = "Elf greaves"


class DwarfBlacksmith(Blacksmith):
    def __init__(self) -> None:
        self.reset()

    def set_helmet(self: Self):
        self._armour.helmet = "Dwarf helmet"

    def set_gauntlets(self: Self):
        self._armour.gauntlets = "Dwarf gauntlets"

    def set_greaves(self: Self):
        self._armour.helmet = "Dwarf greaves"


class Customer:
    def __init__(self: Self, blacksmith: Blacksmith) -> None:
        self.blacksmith = blacksmith

    def buy_minimal_armour(self: Self):
        self.blacksmith.set_helmet()

    def buy_full_armour(self: Self):
        self.blacksmith.set_helmet()
        self.blacksmith.set_greaves()
        self.blacksmith.set_gauntlets()


if __name__ == "__main__":
    elf_customer = Customer(blacksmith=ElfBlacksmith())
    elf_customer.buy_minimal_armour()
    elf_minimal_armour = elf_customer.blacksmith.get_armour()
    print(elf_minimal_armour)

    elf_customer.buy_full_armour()
    elf_full_armour = elf_customer.blacksmith.get_armour()
    print(elf_minimal_armour)

    print("---")

    dwarf_customer = Customer(blacksmith=DwarfBlacksmith())

    dwarf_customer.buy_minimal_armour()
    dwarf_minimal_armour = dwarf_customer.blacksmith.get_armour()
    print(dwarf_minimal_armour)

    dwarf_customer.buy_full_armour()
    dwarf_full_armour = dwarf_customer.blacksmith.get_armour()
    print(dwarf_full_armour)
