data_boolean = "true atau false"
# Mendefinisikan variabel Boolean
is_raining = True
is_weekend = False

# Menggunakan Boolean dalam kondisi
if is_raining:
    print("Bawa payung!")
else:
    print("Tidak perlu payung.")

# Menggunakan operator logika
if is_raining and not is_weekend:
    print("Saya akan bekerja hari ini.")
elif is_weekend or not is_raining:
    print("Saya bisa bersantai hari ini.")

# Contoh fungsi yang mengembalikan Boolean
def is_even(number):
    return number % 2 == 0

# Menggunakan fungsi
number = 4
if is_even(number):
    print(f"{number} adalah angka genap.")
else:
    print(f"{number} adalah angka ganjil.")
