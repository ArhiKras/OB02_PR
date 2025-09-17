class Car():
    def __init__(self, make, model):
        self.public_make = make  # публичный атрибут
        self._protected_model = model  # защищенный атрибут
        self.__private_year = 2022  # приватный атрибут
        
    def public_method(self):
        return f"This is a public method. Make: {self.public_make} {self._protected_model}"
        
    def _protected_method(self):
        return f"This is a protected method. Model: {self._protected_model}"
        
    def __private_method(self):
        return f"This is a private method. Year: {self.__private_year}"
        
class ElectricCar(Car):
    def __init__(self, make, model, battery_size):
        super().__init__(make, model)
        self.battery_size = battery_size
        
    def get_details(self):
        details = f"{self.public_make} {self._protected_model} with a {self.battery_size}-kWh battery"
        return details
        
test = ElectricCar("Tesla", "Model S", 100)

print(test.public_make)  # доступ к публичному атрибуту
print(test.public_method())  # доступ к публичному методу

print(test._protected_model)  # доступ к защищенному атрибуту
print(test._protected_method())  # доступ к защищенному методу

print(test._Car__private_year)  # попытка доступа к приватному методу (ошибка), где Car - имя класса - обходной путь
        