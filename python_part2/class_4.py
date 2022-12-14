class Dog(Animal):
    def __init__(self,name,bark,_leg_count):
        self.name = name
        self.bark = bark
        Animal.__init__(self,_leg_count)

roger = Dog('roger','woof woof','four legs')
print(roger.bark,roger._leg_count, sep='\n')

