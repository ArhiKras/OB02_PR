# Пример инкапсуляции аргументов в Python

class Test_Attr():
    def __init__(self):
        self.public = "Public attribute" # публичный атрибут
        self._protected = "Protected attribute" # защищенный атрибут
        self.__private = "Private attribute" # приватный атрибут
        
    def get_private(self):
        return self.__private # метод для доступа к приватному атрибуту - геттер
    
    def set_private(self, value):
        self.__private = value # метод для изменения приватного атрибута - сеттер
        
test = Test_Attr()

print(test.public) # доступ к публичному атрибуту
print(test._protected) # доступ к защищенному атрибуту
print(test.get_private()) # доступ к приватному атрибуту

test.set_private("New private value") # изменение приватного атрибута через сеттер
print(test.get_private()) # доступ к приватному атрибуту через геттер

# Пример инкапсуляции методов в Python
class Test_Meth():   
    def public_method(self):
        print("\nThis is a public method")     
        
    def _protected_methods(self):
        print("This is a protected method")
        
    def __private_method(self):
        print("This is a private method")
        
    def test_private(self):
        self.__private_method() # вызов приватного метода внутри класса
        
test = Test_Meth()
  
test.public_method() # вызов публичного метода
test._protected_methods() # вызов защищенного метода
test.test_private() # вызов приватного метода