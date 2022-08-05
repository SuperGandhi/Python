class Car():
    def __init__(self, color, brand, model):
        self.color = color
        self.brand = brand
        self.model = model

car_one = Car(color='Blue', brand='Honda', model='R16')
car_two = Car('Red', 'Mazda', 'rx8')
car_one.num_ruedas = 5

print(car_one.color)
