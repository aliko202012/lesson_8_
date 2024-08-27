class Car:
    def __init__(self, make, model, year):
        self.make = make  
        self.model = model  
        self.year = year  

    def __repr__(self):
        return f"{self.make} {self.model} ({self.year})"

class Garage:
    def __init__(self):
        self.cars = []  

    def add_car(self, car):
        self.cars.append(car) 

    def remove_car(self, make, model):
        for car in self.cars:
            if car.make.lower() == make.lower() and car.model.lower() == model.lower():
                self.cars.remove(car)
 
 

    def list_cars(self):
        if not self.cars:
            print("Гараж пуст.")
        else:
            for car in self.cars:
                print(car)  


garage = Garage()


car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2018)
car3 = Car("Ford", "Mustang", 2021)


garage.add_car(car1)
garage.add_car(car2)
garage.add_car(car3)


make_to_remove = "Honda"
model_to_remove = "Civic"
removed = garage.remove_car(make_to_remove, model_to_remove)
if removed:
    print(f"\nАвтомобиль '{make_to_remove} {model_to_remove}' удален.")
else:
    print(f"\nАвтомобиль '{make_to_remove} {model_to_remove}' не найден.")


print("\nОставшиеся автомобили в гараже:")
garage.list_cars()