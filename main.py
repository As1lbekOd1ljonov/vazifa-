# vazifa 1
from collections import namedtuple

users = [
    {"name": "Toxir", "age": 18, "major": "matematika"},
    {"name": "Sobir", "age": 18, "major": "ingliz tili"},
    {"name": "Jobir", "age": 18, "major": "fizika"},
]

Person = namedtuple("Person", ["name","age", "major"])

for user in users:
    person = Person(**user)
    print(f"Name: {person.name} Age: {person.age} Major: {person.major}")

# ===============================================================================================

# vazifa 2
from collections import namedtuple


product = [
    {"product_name": "olma", "price": "12000", "quantity": "15"},
    {"product_name": "banan", "price": "18000", "quantity": "7"},
    {"product_name": "nok", "price": "15000", "quantity": "10"}
]

Mahsolot = namedtuple("Product", ["product_name", "price", "quantity"])

for i in product:
    product = Mahsolot(**i)
    print(f"Product name: {product.product_name} Price: {product.price} Quantity: {product.quantity}")

# ===============================================================================================

# vazifa 3
from collections import namedtuple

city = [
    {"city_name": "Tashkent", "country": "Uzbekistan", "population": "38000000"},
    {"city_name": "Pekin", "country": "Xitoy", "population": "1400000000"},
    {"city_name": "Maskva", "country": "Rossiya", "population": "143000000"},
]

Country = namedtuple("Country", ["city_name", "country", "population"])

cities = [Country(city_name=c["city_name"], country=c["country"], population=int(c["population"])) for c in city]

max_population_city = max(cities, key=lambda c: c.population)

print(f"Eng katta aholi soniga ega shahar: {max_population_city.city_name}, Aholisi: {max_population_city.population}")

# ===============================================================================================

# vazifa 4
from collections import namedtuple

car = [
    {"make": "Tayota", "model": "Corolla", "year": 2020},
    {"make": "GM", "model": "Malibu", "year": 2023},
    {"make": "GM", "model": "Lasetti", "year": 2010}
]

Avtomobil = namedtuple('Avtomobil', ['make', 'model', 'year'])

car_namedtuple = [Avtomobil(**avto) for avto in car]

new_car = max(car_namedtuple, key=lambda avto: avto.year)

print(f"Eng yangi avtomobil: {new_car.make} {new_car.model}, {new_car.year}")

# ===============================================================================================

# vazifa 5
def main():
    def main2():
        return "salom"
    return main2()
print(main())

# ===============================================================================================

# vazifa 6
def salomlashish(name):
    def main():
        return "Assalomu alaykuym"
    return f"{name} {main()}"

print(salomlashish("Toxir"))

# ===============================================================================================

# vazifa 7
def qoshuvchi_funksiya(birinchi_son):
    def qoshish(ikkinchi_son):
        return birinchi_son + ikkinchi_son
    return qoshish
try:
    num1 = int(input("Son kiritin: "))
    num2 = int(input("Son kiritin: "))

    qosh_10 = qoshuvchi_funksiya(num1)
    qosh_5 = qoshuvchi_funksiya(num2)

    print(qosh_10(int(input("son kiritin: "))))
    print(qosh_5(int(input("son kiritin: "))))
except ValueError as e:
    print(e)

# ===============================================================================================

# vazifa 8
def counter():
    counter = 0

    def main():
        nonlocal counter
        counter += 1
        return counter

    return main

counter_funksiya = counter()

print(counter_funksiya())
print(counter_funksiya())
print(counter_funksiya())
print(counter_funksiya())
print(counter_funksiya())
print(counter_funksiya())
print(counter_funksiya())
print(counter_funksiya())

# ===============================================================================================

# vazifa 9
def kvadrat(a):
    def main():
        nonlocal a
        return a ** 2
    return main
try:
    number = int(input("Son kiritin: "))
    kvadrat_funksiya = kvadrat(number)
    print(kvadrat_funksiya())
except  ValueError as e:
    print(e)

# ===============================================================================================

# vazifa 10
ismlar = ["Toxir", "Sobir", "Abdulla"]

def royxat(name):
    global ismlar
    def main():
        nonlocal name
        global ismlar
        ismlar.append(name)
        return ismlar
    return main

name = input("Ism kiritin: ").capitalize()
if name.isalpha():
    royxat_funksiya = royxat(name)
    print(royxat_funksiya())
else:
    print("Ism faqat harfdan iborat bolishi kerak!!!")

# ===============================================================================================

# vazifa 11
def chegirma_foizi(foiz):
    def chegirma(narx):
        chegirma_miqdori = narx * (foiz / 100)
        yangi_narx = narx - chegirma_miqdori
        return yangi_narx
    return chegirma

try:
    narx = int(input("narxni kiritin: "))
    foiz = int(input("foiz kiritin: "))
    yangi_narx = chegirma_foizi(foiz)
    print(f"Yangi narx: {yangi_narx(narx)}")
except ValueError as e:
    print(e)

# ===============================================================================================

# vazifa 12
def kopaytiruvchi():
    natija = 1

    def kopaytir(son):
        nonlocal natija
        natija *= son
        return natija

    return kopaytir

multiplikator = kopaytiruvchi()

print(multiplikator(3))
print(multiplikator(5))
print(multiplikator(7))

# ===============================================================================================

# vazifa 13
def string_qoshuvchi():
    qator = ""

    def qoshish(yangi_qator):
        nonlocal qator
        qator += yangi_qator
        return qator

    return qoshish

qoshuvchi = string_qoshuvchi()

print(qoshuvchi("Salom, "))
print(qoshuvchi("dunyo "))
print(qoshuvchi("Hello "))
print(qoshuvchi("world"))

# ===============================================================================================

# vazifa 14
def sonlar(son):
    def toq_son():
        nonlocal son
        if son % 2 == 1:
            return f"Siz kiritgan toq son: {son}"
        else:
            return "Bu faqat toq son qaytaruvchi funksiya!!!"
    return toq_son
try:
    num = int(input("Son kiritin: "))
    son = sonlar(num)
    print(son())
except ValueError as e:
    print(e)

# ===============================================================================================

# vazifa 15
import math
def number(num):
    def daraja(daraja):
        nonlocal num
        return math.pow(num, daraja)
    return daraja

try:
    num = int(input("Son kiritin: "))
    daraja = int(input("Darajani kiritin: "))
    sonni_darajasi = number(num)
    print(sonni_darajasi(daraja))
except ValueError as e:
    print(e)

# ===============================================================================================

# vazifa 16
def string(text):
    def testkari_string():
         nonlocal text
         text = text[::-1]
         return text
    return testkari_string

matn = input("Matn kiritin: ")
text = string(matn)
print(text())

# ===============================================================================================

# vazifa 17
def create_shopping_cart():
    cart = []

    def add_to_cart(product_name, price):
        cart.append({'name': product_name, 'price': price})
        return f"Mahsulot qo'shildi: {product_name} - {price} so'm"

    def get_total():
        total = sum(item['price'] for item in cart)
        return f"Umumiy summa: {total} so'm"

    return add_to_cart, get_total

add_to_cart, get_total = create_shopping_cart()

print(add_to_cart("Olma", 5000))
print(add_to_cart("Non", 3000))

print(get_total())

# ===============================================================================================

# vazifa 18
def create_price_list():
    prices = []

    def add_price(product_name, price):
        prices.append({'name': product_name, 'price': price})
        return f"Mahsulot qo'shildi: {product_name} - {price} so'm"

    def get_prices():
        return prices

    return add_price, get_prices
add_price, get_prices = create_price_list()

print(add_price("Olma", 5000))
print(add_price("Banan", 7000))

for product in get_prices():
    print(f"{product['name']}: {product['price']} so'm")