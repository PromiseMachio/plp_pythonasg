class Car:
    def __init__(self, model="Mustang", brand="Ford", year=1964, color="red"):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        
    def start(self):
        print(f"The {self.brand} {self.model} is starting")

    def bike(self):
        print(f"The {self.brand} {self.model} bike is revving")

# create car object with default values
mycar = Car()

# create bike object with custom values
mybike = Car("BM150", "Honda", 2023, "black")

# call the methods
mycar.start()
mybike.bike()

class person:
    def __init__(self, name, age):
         self.name = name 
         self.age = age 
    
p1 = person("Machio Promise", 18)
p2 = person("John Mbandu", 20)
p3 = person("Willy Hambuger", 24)

print(p1.name)
print(p2.age)
print(p3.name)
print(p1.age)

class dog:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def __str__(self):
        return(f"{self.name} is {self.age} years old and is a {self.gender}")
    
dog1 = dog("Rex", 5, "male")
dog2 = dog("Luna", 3, "female")
dog3 = dog("Buddy", 4, "male")
dog4 = dog("Daisy", 6, "female")

print(dog1)