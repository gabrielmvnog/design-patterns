from abc import ABC, abstractmethod
from typing import Self


class Attack(ABC):
    @abstractmethod
    def exec(self: Self):
        pass


class MeeleAttack(Attack):
    def exec(self: Self):
        print("Meele attack!")


class RangeAttack(Attack):
    def exec(self: Self):
        print("Ranged attack!")


class Battle:
    def first_attack(self: Self, attack: Attack):
        self.first = attack

    def second_attack(self: Self, attack: Attack):
        self.second = attack

    def start(self: Self):
        self.first.exec()

        self.second.exec()


if __name__ == "__main__":
    battle = Battle()

    battle.first_attack(RangeAttack())

    battle.second_attack(MeeleAttack())

    battle.start()
