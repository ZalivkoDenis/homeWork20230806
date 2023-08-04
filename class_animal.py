from abc import abstractmethod
from abc import ABC


class Animal(ABC):
    """
    Базовый класс для животных
    """

    def __init__(self, name: str, color: str = None):
        self.name = name
        self.color = color

    @property
    def name(self):
        """
        Имя (кличка) животного
        """
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def color(self) -> str:
        return self._color

    @color.setter
    def color(self, color: str):
        self._color = color

    @property
    @abstractmethod
    def animal_type(self) -> str: return "Animal"

    @abstractmethod
    def do_voice(self) -> str:
        """
        Animal voice-to-text converter.
        :return: Animal voice!
        """
        return ""

    def __str__(self):
        return (f'Type: {self.animal_type} Name: {self.name} '
                f'Color: {"not implement" if self.color is None else self.color}')
