class Animal:
    def make_sound(self):
        print("Some generic sound")

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

# Створення об'єктів
animal = Animal()
dog = Dog()

# Виклик методу
animal.make_sound()  # Output: Some generic sound
dog.make_sound()     # Output: Woof!
