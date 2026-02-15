from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "Galaxy S23", "+79123456789"),
    Smartphone("Apple", "iPhone 15 Pro", "+79234567890"),
    Smartphone("Xiaomi", "Redmi Note 12", "+79345678901"),
    Smartphone("Huawei", "P60 Pro", "+79456789012"),
    Smartphone("Realme", "GT Neo 5", "+79567890123"),
]

for smartphone in catalog:
    print(
        f"{smartphone.brand} - {smartphone.model}. {smartphone.phone_number}"
    )
