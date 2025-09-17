class Bird(): # родительский класс
    def __init__(self, name, voice, color):
        self.name = name
        self.voice = voice
        self.color = color
        
    def fly(self):
        print(f"{self.name} is flying")
        
    def eat(self):
        print(f"{self.name} is eating")
        
    def sing(self):
        print(f"{self.name} says {self.voice}")
        
    def info(self):
        print(f"Name: {self.name}, Color: {self.color}, Voice: {self.voice}")
        
    
class Pigeon(Bird): # дочерний класс
    def __init__(self, name, voice, color, favorite_food): # конструктор дочернего класса
        super().__init__(name, voice, color) # вызов конструктора родительского класса, для использования его атрибутов и методов
        self.favorite_food = favorite_food
        
    def walk(self):
        print(f"{self.name} is walking")
        

bird1 = Pigeon("Gosha", "ur-ur", "grey", "worms") # создание объекта класса Pigeon, наследующего от Bird   
bird2 = Bird("Kesha", "ki-ki", "green") # создание объекта класса Bird   

bird1.sing()
bird1.info()
bird1.walk()

bird2.info()    