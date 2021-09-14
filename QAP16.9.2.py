class Square:
    def __init__(self, a):
        self.a = a
    def get_area(self):
        return f'Площадь квадрата = {self.a**2}'

square = Square(6)

print(square.get_area())
    