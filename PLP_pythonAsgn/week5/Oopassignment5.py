# Base Class
class Kingdom:
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat

    def info(self):
        return f"{self.name} lives in {self.habitat}"

    def move(self):
        return f"{self.name} is moving in its own way."


# Subclass: Animal
class Animal(Kingdom):
    def __init__(self, name, habitat, sound):
        super().__init__(name, habitat)  # Inherit from Kingdom
        self.sound = sound

    def make_sound(self):
        return f"{self.name} says {self.sound}"

    # Polymorphism
    def move(self):
        return f"{self.name} runs swiftly on land 🐆."


# Subclass: Bird
class Bird(Kingdom):
    def __init__(self, name, habitat, wing_span):
        super().__init__(name, habitat)
        self.wing_span = wing_span

    def details(self):
        return f"{self.name} has a wingspan of {self.wing_span} meters."

    # Polymorphism
    def move(self):
        return f"{self.name} flies high in the sky 🕊️."


# Subclass: Fish
class Fish(Kingdom):
    def __init__(self, name, habitat, size):
        super().__init__(name, habitat)
        self.size = size

    def details(self):
        return f"{self.name} is {self.size} cm long."

    # Polymorphism
    def move(self):
        return f"{self.name} swims gracefully in water 🐠."


# ---------- TESTING ----------
lion = Animal("Lion", "Savannah", "Roar")
eagle = Bird("Eagle", "Mountains", 2.1)
shark = Fish("Shark", "Ocean", 350)

creatures = [lion, eagle, shark]

for c in creatures:
    print(c.info())
    print(c.move())     # Polymorphism in action
    if isinstance(c, Animal):
        print(c.make_sound())
    elif isinstance(c, Bird):
        print(c.details())
    elif isinstance(c, Fish):
        print(c.details())
    print("-" * 40)
