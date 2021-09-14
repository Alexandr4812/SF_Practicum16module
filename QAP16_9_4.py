class GuestList:
    def __init__(self, name, city, status):
        self.name = name
        self.city = city
        self.status = status
    def invited(self):
        return f'{self.name}, {self.city}, статус: {self.status}'


