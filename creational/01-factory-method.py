from abc import ABC, abstractmethod
from typing import Self


class Creator(ABC):
    @abstractmethod
    def create(self: Self):
        return ...
    