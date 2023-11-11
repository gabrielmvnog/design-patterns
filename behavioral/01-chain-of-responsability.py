from dataclasses import dataclass, field
from typing import List, Self, Type


@dataclass
class Equipament:
    type_: str

    def __repr__(self) -> str:
        return f"{self.type_} equipament"


@dataclass
class Helmet(Equipament):
    def __repr__(self) -> str:
        return f"{self.type_} helmet"

    def block(self: Self, attack: str):
        if attack == "Meele & Range":
            return "Helmet blocked!"


@dataclass
class Gauntlets(Equipament):
    def __repr__(self) -> str:
        return f"{self.type_} gauntlets"

    def block(self: Self, attack: str):
        if attack == "Range":
            return "Gauntlets blocked!"


@dataclass
class Greaves(Equipament):
    def __repr__(self) -> str:
        return f"{self.type_} greaves"

    def block(self: Self, attack: str):
        if attack == "Meele":
            return "Greaves blocked!"


@dataclass
class Armour(Equipament):
    equipaments: List[Equipament] = field(default_factory=list)

    def add(self: Self, equipament: Type[Equipament]):
        self.equipaments.append(equipament(self.type_))

    def block(self: Self, attack: str):
        for equipament in self.equipaments:
            result = equipament.block(attack)

            if result:
                return result

        return "Atack was effective!"


if __name__ == "__main__":
    armour = Armour("Golder")

    armour.add(Greaves)
    armour.add(Gauntlets)
    armour.add(Helmet)

    for attack in ["Meele & Range", "Magic" , "Meele", "Range"]:
        result = armour.block(attack)

        print(result)
