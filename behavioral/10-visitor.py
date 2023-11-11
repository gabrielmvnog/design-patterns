from abc import ABC, abstractmethod
from dataclasses import asdict, dataclass
import json
from pprint import pprint
from typing import Self


class Exporter(ABC):
    @abstractmethod
    def export_normal_player(self: Self, user: "User"):
        pass

    @abstractmethod
    def export_game_master(self: Self, user: "User"):
        pass


class ExporterJSON(Exporter):
    def export_normal_player(self: Self, user: "User"):
        pprint(json.dumps(asdict(user)))

    def export_game_master(self: Self, user: "User"):
        pprint(f"GAME MASTER: {json.dumps(asdict(user))}")


class ExporterDict(Exporter):
    def export_normal_player(self: Self, user: "User"):
        pprint(asdict(user))

    def export_game_master(self: Self, user: "User"):
        pprint(f"GAME MASTER: {asdict(user)}")


@dataclass
class User(ABC):
    name: str

    @abstractmethod
    def export(self: Self, exporter: Exporter) -> None:
        pass


@dataclass
class NormalPlayer(User):
    def export(self: Self, exporter: Exporter) -> None:
        exporter.export_normal_player(self)


@dataclass
class GameMaster(User):
    def export(self: Self, exporter: Exporter) -> None:
        exporter.export_game_master(self)


if __name__ == "__main__":
    normal_player = NormalPlayer("Normal")
    game_master = GameMaster("Master")

    normal_player.export(ExporterJSON())
    game_master.export(ExporterJSON())

    print(" --- ")

    normal_player.export(ExporterDict())
    game_master.export(ExporterDict())
