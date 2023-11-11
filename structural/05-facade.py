from dataclasses import dataclass
from typing import Self


@dataclass
class Helmet:
    type_: str

    def __repr__(self) -> str:
        return f"{self.type_} helmet"


@dataclass
class Gauntlets:
    type_: str

    def __repr__(self) -> str:
        return f"{self.type_} gauntlets"


@dataclass
class Greaves:
    type_: str

    def __repr__(self) -> str:
        return f"{self.type_} greaves"


@dataclass
class Armour:
    helmet: Helmet
    greaves: Greaves
    gauntlets: Gauntlets


class Blacksmith:
    def create_healmet(self: Self, type_: str) -> Helmet:
        return Helmet(type_)

    def create_greaves(self: Self, type_: str) -> Greaves:
        return Greaves(type_)

    def create_gauntlets(self: Self, type_: str) -> Gauntlets:
        return Gauntlets(type_)

    def create_armour(self: Self, type_: str) -> Armour:
        helmet = self.create_healmet(type_)
        greaves = self.create_greaves(type_)
        gauntlets = self.create_gauntlets(type_)

        return Armour(helmet=helmet, greaves=greaves, gauntlets=gauntlets)


if __name__ == "__main__":
    blacksmith = Blacksmith()

    golden_armour = blacksmith.create_armour("Golden")
    print(golden_armour)

    silver_armour = blacksmith.create_armour("Silver")
    print(silver_armour)
