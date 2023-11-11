from abc import ABC, abstractmethod
from typing import List, Self


class User(ABC):
    @abstractmethod
    def read(self: Self, message: str, global_message: bool):
        pass


class Player:
    def read(self: Self, message: str, global_message: bool):
        if global_message:
            print(f"Player read: {message}")


class GameMaster:
    def read(self: Self, message: str, global_message: bool):
        print(f"GameMaster read: {message}")


class Server:
    def __init__(self) -> None:
        self.users: List[User] = []

    def chat(self: Self, message: str, global_message: bool = True) -> None:
        for user in self.users:
            user.read(message, global_message)

    def login(self: Self, user):
        self.users.append(user)


if __name__ == "__main__":
    server = Server()

    player = Player()
    server.login(player)
    game_master = GameMaster()
    server.login(game_master)

    server.chat("Hello everyone")
    
    print("---")
    
    server.chat("Hello GameMasters", global_message=False)
