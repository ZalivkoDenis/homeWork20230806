from class_animal import Animal


class Cat(Animal):
    """
    Класс, определяющий поведение кота )
    """

    def __init__(self, name):
        super().__init__(name)
        self._animal_type = 'Cat'

    def do_voice(self):
        return "Say miauuuu! I'm cat!"

    def __str__(self):
        return super().__str__()