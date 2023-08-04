from class_animal import Animal


class Cat(Animal):
    """
    Класс, определяющий поведение кота )
    """

    @property
    def animal_type(self) -> str: return "Cat"

    def do_voice(self):
        return "мяу"
