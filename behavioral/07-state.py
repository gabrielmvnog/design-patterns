from typing import Self


class Mage:
    @property
    def element(self: Self):
        return self._element

    @element.setter
    def element(self: Self, var: str):
        self._element = var

    def attack(self: Self):
        if self._element == "water":
            print(f"Attack: {self._element}")

        if self._element == "fire":
            print(f"Run from: {self._element}")

if __name__ == "__main__":
    mage = Mage()

    mage.element = "water"
    mage.attack()

    mage.element = "fire"
    mage.attack()
