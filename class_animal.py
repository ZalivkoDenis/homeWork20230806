from abc import abstractmethod


class Animal:
    """
    Базовый класс для животных
    """

    def __init__(self, name: str):
        self.name = name
        self._animal_type = 'Animal'

    @property
    def name(self):
        """
        Имя (кличка) животного
        """
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    animal_type = property(fget=lambda self: self._animal_type)

    @abstractmethod
    def do_voice(self) -> str:
        """
        Animal voice-to-text converter.
        :return: Animal voice!
        """
        pass

    def __str__(self):
        return f'Type: {self.animal_type} Name: {self.name}'
