from models.product import Product
from models.food_product import FoodProduct
from models.digital_product import DigitalProduct

product = Product("P001", "Indomie", 3000, 20)
print("Produk pertama:", product.name)
print("Subtotal 2 Indomie =", product.subtotal(2))

print()

products = [ 
    Product("P001", "Indomie", 3000, 20),
    FoodProduct("F001", "Roti", 7000, 8, "2026-12-01"),
    DigitalProduct("D001", "E-Book Python", 50000, 99),
]
print("=========================")
print("     SIMPLE CASHIER")
print("=========================")
print() 

print("--- Polymorphism ---")

# Satu list berisi tiga jenis object, satu loop, tiga hasil berbeda.
# main.py tidak perlu tahu jenis produknya.

for item in products:
    print(item.code, "|", item.get_description())
    print(item.code, item.name, item.price, item.stock)

print()
print("--- Yang diwarisi dari Product ---")

roti = products[1]

# subtotal() tidak ditulis ulang di FoodProduct, tetapi tetap bisa dipakai.
print("Subtotal 3 Roti:", roti.subtotal(3))
# expiry_date hanya dimiliki FoodProduct.
print("Kedaluwarsa Roti:", roti.expiry_date)

print("--- Masalah Minggu 02 ---")

indomie = products[0]

# Di Minggu 02 baris ini mengubah harga menjadi negatif tanpa perlawanan.
# Sekarang price hanya bisa dibaca, tidak bisa ditulis.
try:
    indomie.price = -5000
except ValueError:
    print("Menulis langsung ke price ditolak (property tanpa setter).")

print()

print("--- Encapsulation Minggu 03 tetap berlaku di subclass ---")

try:
    roti.price = 1
except AttributeError:
    print("FoodProduct.price tetap read-only.")

try:
    roti.change_price(-1000)
except ValueError as error:
    print("FoodProduct.change_price(-1000) ->", error)

try:
    roti.reduce_stock(999)
except ValueError as error:
    print("FoodProduct.reduce_stock(999)   ->", error)

roti.reduce_stock(3)

print("Stock Roti setelah terjual 3:", roti.stock)

print("Aturan ditulis sekali di Product, dipakai semua turunannya.")

print("--- Perubahan lewat method ---")

indomie.change_price(3500)

print("Harga baru:", indomie.price)

indomie.reduce_stock(5)
print("Stock setelah terjual 5:", indomie.stock)
print()
print("--- Setiap aturan diuji ---")

try:
    indomie.change_price(-5000)
except ValueError as error:
    print("change_price(-5000) ->", error)

try:
    indomie.reduce_stock(0)
except ValueError as error:
    print("reduce_stock(0)     ->", error)

try:
    indomie.reduce_stock(-10)
except ValueError as error:
    print("reduce_stock(-10)    ->", error)

try:
    indomie.reduce_stock(999)
except ValueError as error:
    print("reduce_stock(999)   ->", error)

try:
    indomie.price=-5000
except ValueError as error:
    print("indomie.price=-5000 ->", error)
    
try:
    indomie.price=5000
except AttributeError as error:
    print("indomie.price=5000 ->", error)

print()
print("Harga akhir:", indomie.price, "| Stock akhir:", indomie.stock)
print("Percobaan yang gagal tidak mengubah apa pun.") 