from typing import Self


class Armour:
    name: str

    @property
    def helmet(self):
        return self._helmet

    @helmet.setter
    def helmet(self, var: bool) -> None:
        self._helmet = var


class SimpleArmour(Armour):
    name: str = "Simple armour"


class GoldenArmour(Armour):
    name: str = "Golden armour"


class Person:
    def __init__(self: Self, armour: Armour):
        self.armour = armour

    def _echo_helmet(self: Self):
        print(f"{self.armour.name} is on? {self.armour.helmet}")

    def put_helmet(self: Self):
        self.armour.helmet = True
        self._echo_helmet()

    def remove_helmet(self: Self):
        self.armour.helmet = False
        self._echo_helmet()


if __name__ == "__main__":
    person = Person(armour=SimpleArmour())

    person.put_helmet()
    person.remove_helmet()
    
    print("---")

    person = Person(armour=GoldenArmour())

    person.put_helmet()
    person.remove_helmet()
