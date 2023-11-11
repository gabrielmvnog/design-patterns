from typing import Any, Iterable, Iterator, List, Self


class MovementFlow(Iterator):
    def __init__(self: Self, movements: List[str]) -> None:
        self._position = 0
        self._movements = movements

    def __next__(self: Self) -> Any:
        try:
            next_ = self._movements[self._position]
            self._position += 1
        except IndexError:
            raise StopIteration()

        return next_


class BattleMoves(Iterable):
    def __init__(self: Self) -> None:
        self._movements: List[str] = []

    def __iter__(self: Self) -> Iterator:
        return MovementFlow(self._movements)

    def add_movement(self: Self, movement: str):
        self._movements.append(movement)


if __name__ == "__main__":
    battle_moves = BattleMoves()

    battle_moves.add_movement("Meele attack")
    battle_moves.add_movement("Ranged attack")
    battle_moves.add_movement("Magic attack")

    print(" > ".join(battle_moves))
