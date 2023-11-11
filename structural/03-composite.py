from typing import List, Self


class Weapon:
    def __init__(self: Self, name: str) -> None:
        self.name = name

    def __repr__(self) -> str:
        return f"Weapon: {self.name}"


class CompositeWeapon(Weapon):
    def __init__(self: Self, name: str) -> None:
        super().__init__(name)
        self.weapons: List[Weapon] = []

    def add(self: Self, weapon: Weapon) -> None:
        self.weapons.append(weapon)

    def list_weapons(self: Self):
        weapons = []

        for weapon in self.weapons:
            if isinstance(weapon, CompositeWeapon):
                weapons.append(weapon.list_weapons())
            else:
                weapons.append(weapon)

        return weapons


if __name__ == "__main__":
    double_sword = CompositeWeapon("Double sword")

    sword_one = Weapon("Sword one")
    sword_two = Weapon("Sword two")

    double_sword.add(sword_one)
    double_sword.add(sword_two)

    print(double_sword.list_weapons())

    double_sword_and_mace = CompositeWeapon("Double sword and mace")

    mace = Weapon("Mace")

    double_sword_and_mace.add(double_sword)
    double_sword_and_mace.add(mace)

    print(double_sword_and_mace.list_weapons())
