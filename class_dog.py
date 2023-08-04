from class_animal import Animal


class Dog(Animal):
    """
    Класс, определяющий поведение собаки.
    """

    @property
    def animal_type(self) -> str: return "Dog"

    def do_voice(self):
        return "гав"

