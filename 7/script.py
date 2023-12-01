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

    # "Метод класу", який працює зі змінними класу
    @classmethod
    def get_count(cls):
        return cls.count

    # Альтернативний конструктор за допомогою методу класу
    @classmethod
    def create_from_string(cls, product_string):
        name, category, price_str, discount_str = product_string.split(',')
        price = float(price_str)
        discount = float(discount_str)
        return cls(name, category, price, discount)

    # Статичний метод, який просто виводить повідомлення
    @staticmethod
    def print_message():
        print("This is a static method.")

# Створення об'єктів класу Product
product1 = Product("Laptop", "Electronics", 1200, 10)
product2 = Product("Book", "Education", 20)
product3 = Product("Headphones", "Electronics", 100, 5)

# Вивід опису та лічильника
print(product1.generate_description())
print(f"Number of created objects: {Product.get_count()}")

# Виклик альтернативного конструктора
product_string = "Keyboard,Electronics,50,8"
product4 = Product.create_from_string(product_string)
print(product4.generate_description())

# Виклик статичного методу
Product.print_message()
