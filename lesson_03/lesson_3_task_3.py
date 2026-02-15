from address import Address
from mailing import Mailing

sender_address = Address("125009", "Москва", "Тверская", "7", "25")

recipient_address = Address(
    "603000", "Нижний Новгород", "Большая Покровская", "40", "12"
    )

mailing = Mailing(
    to_address=recipient_address,
    from_address=sender_address,
    cost=350,
    track="RU123456789RU"
)

print(
    f"Отправление {mailing.track} из {mailing.from_address.index}, "
    f"{mailing.from_address.city}, {mailing.from_address.street}, "
    f"{mailing.from_address.house} - {mailing.from_address.apartment} "
    f"в {mailing.to_address.index}, {mailing.to_address.city}, "
    f"{mailing.to_address.street}, {mailing.to_address.house} - "
    f"{mailing.to_address.apartment}. Стоимость {mailing.cost} рублей."
)
