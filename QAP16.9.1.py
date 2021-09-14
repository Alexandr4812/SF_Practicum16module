from math import pi

class Figures:
    def __init__(self, name):
        self.name = name

class Rectangle(Figures):
    def __init__(self, name, a, b):
        super().__init__(name)
        self.a = a
        self.b = b
    def get_area_rectangle(self):
        return f'Площадь прямоугольника = {self.a * self.b}'
    def get_info_rectangle(self):
        return f'''
Информация о фигуре:
Название фигуры: {self.name}
Сторона "a" прямоугольника = {self.a}
Сторона "b" прямоугольника = {self.b}'''

class Square(Figures):
    def __init__(self, name, a):
        super().__init__(name)
        self.a = a
    def get_area_square(self):
        return f'\nПлощадь квадрата = {self.a ** 2}'
    def get_info_squre(self):
        return f'''
Информация о фигуре:
Название фигуры: {self.name}
Стороны квадрата = {self.a}'''

class Circle(Figures):
    def __init__(self, name, r):
        super().__init__(name)
        self.r = r
    def get_area_circle(self):
        sr = pi * self.r ** 2
        sr = float('{:.2f}'.format(sr))
        return f'\nПлощадь круга = {sr}'
    def get_info_circle(self):
        return f'''
Информация о фигуре:
Название фигуры: {self.name}
Радиус круга = {self.r}'''

rectangle = Rectangle('прямоугольник', 6, 5)
print(rectangle.get_area_rectangle())
print(rectangle.get_info_rectangle())

square = Square('квадрат', 6)
print(square.get_area_square())
print(square.get_info_squre())

circle = Circle('круг', 6)
print(circle.get_area_circle())
print(circle.get_info_circle())