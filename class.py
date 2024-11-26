class Cars:
    def __init__(self, brand, colour, weight):
        self.brand = brand
        self.colour = colour 
        self.weight = weight
        pass
    def __str__(self):
        return f"{self.brand}({self.colour}), ({self.weight})"
        pass
    def myfunc(self):
        print("This is a good choice ", self.brand)

        

C1 = Cars("Toyota", "black", 300)
C2 = Cars("Nisaan", "green", 450)
C3 = Cars("Mazda", "red", 560)

print(C2.weight)
print(C2)
print(C3.colour)


C1 = Cars("Toyota", "black", 300)
C1.myfunc()
