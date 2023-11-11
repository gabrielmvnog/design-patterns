from typing import Self


class Sword:
    def __init__(self) -> None:
        self.damage = 100

    def attack(self: Self) -> None:
        print(f"Sword attack, damage:{self.damage}")


class SwordDecorator(Sword):
    def __init__(self, sword: Sword) -> None:
        self.damage = sword.damage


class PlasticDecorator(SwordDecorator):
    def __init__(self, sword: Sword) -> None:
        self.damage = sword.damage - 10


class CottonDecorator(SwordDecorator):
    def __init__(self, sword: Sword) -> None:
        self.damage = sword.damage - 50


if __name__ == "__main__":
    sword = Sword()

    sword = PlasticDecorator(sword)
    sword = CottonDecorator(sword)

    sword.attack()
