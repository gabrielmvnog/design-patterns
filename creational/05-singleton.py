from typing import Self


class SingletonShield:
    _instance = None

    def __new__(cls) -> Self:
        if not cls._instance:
            cls._instance = super().__new__(cls)

        return cls._instance


if __name__ == "__main__":
    shield_one = SingletonShield()
    shield_two = SingletonShield()

    assert id(shield_one) == id(shield_two)

    print("They'are the same shield!!")
    print(shield_two)
    print(shield_two)
