# Импорт модулей
from Address_class import Address
from Mailing_class import Mailing

to_address = Address("123456", "Москва", "Тверская", "10", "15")
from_address = Address("654321", "Санкт-Петербург", "Невский проспект", "20", "5")

mailing = Mailing(to_address, from_address, 500, "AB123456789RU")

print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, "
      f"{mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} "
      f"в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, "
      f"{mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")