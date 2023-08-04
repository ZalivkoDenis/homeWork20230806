# ШАГ. Д/з по сроку 06/08/2023 (полиморфизм) © Денис Заливко
"""
Создать класс Animal: name, color
Создать класс Cat(Animal): свойства(get, set) по всем атрибутам, метод выводит мяу
Создать класс Dog(Animal): свойства(get, set) по всем атрибутам, метод выводит гав
"""

from class_animal import Animal
from class_cat import Cat
from class_dog import Dog

if __name__ == "__main__":
    animals: list[Animal] = [Cat("Мурзик", "Рыжий"), Dog("Мухтар"), Cat("Васька", "Полосатый")]

    # Ошибка, т.к. класс Animal абстрактный!
    # animals.append(Animal('Unknown Animal'))

    for item in animals:
        print(item, 'Say:', item.do_voice())
