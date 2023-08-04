from class_animal import Animal


class Dog(Animal):
    """
    Класс, определяющий поведение собаки.
    """

    def __init__(self, name):
        super().__init__(name)
        self._animal_type = 'Dog'

    def do_voice(self):
        return "Say uafffff! I'm dog!"

    def __str__(self):
        return super().__str__()