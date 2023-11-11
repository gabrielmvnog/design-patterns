from typing import Self


class Weapon:
    def attack(self: Self) -> None:
        print("Sword attack")


class Sword(Weapon):
    def attack(self: Self) -> None:
        print("Sword attack")


class Shield:
    def block(self: Self) -> None:
        print("Shield block")


class ShieldAdaptedToAttack(Weapon):
    def __init__(self, shield: Shield) -> None:
        self.sword = sword

    def attack(self: Self) -> None:
        print("Shield attack")


class Person:
    def use_weapon(self: Self, weapon: Weapon):
        weapon.attack()


if __name__ == "__main__":
    person = Person()
    shield = Shield()
    sword = Sword()

    person.use_weapon(sword)

    try:
        person.use_weapon(shield)  # Cant do the attack
    except AttributeError as err:
        print(err)

    spiked_shield = ShieldAdaptedToAttack(shield)
    person.use_weapon(spiked_shield)  # Now we can use the shield to attack
