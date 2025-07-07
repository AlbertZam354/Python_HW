from smartphone import Smartphone

phone1 = Smartphone("Apple", "16 Pro Max", "+79271111111")
phone2 = Smartphone("Lenovo", "10", "+79272222222")
phone3 = Smartphone("Honor", "Deluxe", "+79273333333")
phone4 = Smartphone("Samsung", "Galaxy S40", "+79274444444")
phone5 = Smartphone("Redmi", "Note", "+79275555555")

catalog = [phone1, phone2, phone3, phone4, phone5]

for phones in catalog:
    print(phones)