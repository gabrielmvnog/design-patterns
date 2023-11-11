from copy import copy
from typing import Self


class ElfShield:
    def __init__(self: Self, block: int) -> None:
        self.block = block

    def __repr__(self) -> str:
        return f"<ElfShield block={self.block}>"


if __name__ == "__main__":
    shield = ElfShield(10)
    another_shield = copy(shield)

    assert shield != another_shield

    print(shield)
    print(another_shield)
