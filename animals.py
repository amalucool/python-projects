class animals:
    def __init__(self, biome, diet):
        self.biome = biome 
        self.diet = diet 
    def sound(self):
        print("Meow")

class Cat(animals):
    pass

class Dog(animals):
    def sound(self):
        print("Bow Bow")

class Bird(animals):
    def sound(self):
        print("Chirp Chirp")

cat1 = Cat("Domestic", "Can food")
dog1 = Dog("Artic", "Wild Fish")
bird1 = Bird("Tropical Forrest", "Wild Berries")

for x in (cat1, dog1, bird1):
  print(x.biome)
  print(x.diet)
  x.sound()
    