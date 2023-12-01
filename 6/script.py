class Product:
    # Змінна класу для лічильника
    count = 0

    def __init__(self, name, category, price, discount=0):
        self.name = name
        self.category = category
        self.price = price
        self.discount = discount

        # Атрибут, який створюється на основі інших
        self.discounted_price = self.calculate_discounted_price()

        # Збільшення лічильника при кожному створенні об'єкта
        Product.count += 1

    def calculate_discounted_price(self):
        return self.price - (self.price * self.discount / 100)

    def generate_description(self):
        return f"{self.name} is a {self.category} priced at ${self.price}. After a {self.discount}% discount, the new price is ${self.discounted_price}."

# Створення об'єктів класу Product
product1 = Product("Laptop", "Electronics", 1200, 10)
product2 = Product("Book", "Education", 20)
product3 = Product("Headphones", "Electronics", 100, 5)

# Виклик методу для генерації опису об'єкта
description = product1.generate_description()

# Виведення опису та лічильника створених об'єктів
print(description)
print(f"Number of created objects: {Product.count}")
