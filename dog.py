class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f"{self.name} is {self.age} years old.")

    def get_info(self):
        print(f"{self.name} has a {self.coat_color} coat.")


class JackRussellTerrier(Dog):
    def bark(self):
        print("Woof! Woof!")

    def hunt(self):
        print("I love to hunt!")


class Bulldog(Dog):
    def bark(self):
        print("Woof!")

    def guard(self):
        print("I'm a great guard dog.")


# create objects
dog1 = Dog("Buddy", 3, "brown")
dog2 = JackRussellTerrier("Jack", 5, "white")
dog3 = Bulldog("Bully", 2, "black")

# call methods
dog1.description()
dog1.get_info()

dog2.description()
dog2.get_info()
dog2.bark()
dog2.hunt()

dog3.description()
dog3.get_info()
dog3.bark()
dog3.guard()
