perbandingan = "saya suka perbandingan,saya suka belajar python"
#print (perbandingan)#
# Mendefinisikan variabel
x = 15
y = 25
z = 15

# Menggunakan operator perbandingan
print("Perbandingan nilai:")
print("x == y:", x == y)  # Sama dengan
print("x != y:", x != y)  # Tidak sama dengan
print("x < y:", x < y)    # Kurang dari
print("x > y:", x > y)    # Lebih dari
print("x <= z:", x <= z)  # Kurang dari atau sama dengan
print("x >= z:", x >= z)  # Lebih dari atau sama dengan

# Menggunakan perbandingan dalam kondisi
if x < y:
    print("x lebih kecil dari y")
else:
    print("x tidak lebih kecil dari y")

# Menggunakan perbandingan untuk menentukan nilai terbesar
def find_largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Contoh pemanggilan fungsi
largest = find_largest(x, y, z)
print("Nilai terbesar di antara x, y, dan z adalah:", largest)
