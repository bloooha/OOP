class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} says {self.sound}")


class Mammal(Animal):
    def __init__(self, name, sound, num_legs):
        super().__init__(name, sound)
        self.num_legs = num_legs

    def describe(self):
        print(f"{self.name} is a mammal with {self.num_legs} legs")


class Dog(Mammal):
    def __init__(self, name, breed):
        super().__init__(name, "Woof", 4)
        self.breed = breed

    def greet(self, other_dog):
        print(f"{self.name} greets {other_dog.name}")


class Cat(Mammal):
    def __init__(self, name, color):
        super().__init__(name, "Meow", 4)
        self.color = color

    def play(self, other_cat):
        print(f"{self.name} plays with {other_cat.name}")


# Використання методів об’єктів-представників іншого дочірнього класу
my_dog = Dog("Buddy", "Golden Retriever")
my_cat = Cat("Whiskers", "Gray")

my_dog.greet(my_cat)  # Виклик методу greet об'єкта класу Dog
my_cat.play(my_dog)   # Виклик методу play об'єкта класу Cat

# Перевірка чи об'єкти є представниками певних класів
print(isinstance(my_dog, Dog))    # True
print(isinstance(my_dog, Mammal)) # True
print(isinstance(my_dog, Animal)) # True

# Перевірка чи класи є підкласами інших класів
print(issubclass(Dog, Mammal))   # True
print(issubclass(Mammal, Animal)) # True
