class Vehicle:
    def __init__(self, brand:str, model:str)->None:
        self.brand=brand
        self.model=model

    def get_info(self):
        return f"{self.brand}-{self.model}"


Car1=Vehicle("Benz","S400")

class Car(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand, model)
        self.year=year

    def get_info(self):
        return f"{super().get_info()}-{self.year}"

Car2=Car("Hyundai","Genesis","2020")
print(Car1.get_info())
print(Car2.get_info())
