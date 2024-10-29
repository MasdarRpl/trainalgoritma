list = "aldi,ritman,nawir,rahmat"
print (list)
# Mendefinisikan list
fruits = ["apel", "pisang", "jeruk", "mangga"]

# Mengakses elemen dalam list
print("Buah pertama:", fruits[0])  # Mengakses buah pertama

# Menambahkan elemen ke dalam list
fruits.append("anggur")
print("List setelah ditambahkan:", fruits)

# Menghapus elemen dari list
fruits.remove("pisang")
print("List setelah dihapus:", fruits)

# Menghitung panjang list
length = len(fruits)
print("Jumlah buah dalam list:", length)

# Mengiterasi elemen dalam list
print("Daftar buah:")
for fruit in fruits:
    print(fruit)

# Mengurutkan list
fruits.sort()
print("List buah setelah diurutkan:", fruits)

# Membalikkan urutan list
fruits.reverse()
print("List buah setelah dibalik:", fruits)
