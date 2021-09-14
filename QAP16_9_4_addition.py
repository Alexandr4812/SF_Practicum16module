from QAP16_9_4 import GuestList

Petrov = GuestList('Иван Петров', 'г.Москва', '"Наставник"')
Krasnov = GuestList('Аркадий Краснов', 'г.Воронеж', '"Ученик"')
Kazakova = GuestList('Анастасия Казакова', 'г.Варкута', '"Ученик"')

guests = [Petrov, Krasnov, Kazakova]

for guest in guests:
    print(guest.invited())