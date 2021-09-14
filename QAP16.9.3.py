class Clients:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def get_client_info(self):
        return f'''
Клиент "{self.name}"
Баланс: {self.balance} рублей.'''

client = Clients('Иван Петров', 50)
print(client.get_client_info())