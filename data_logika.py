logika = "saya suka logika, saya suka belajar python"
print ("logika")
# Mendefinisikan beberapa variabel Boolean
is_raining = True
is_weekend = False
has_umbrella = True

# Menggunakan operator logika AND, OR, dan NOT
if is_raining and has_umbrella:
    print("Saya akan keluar dengan payung.")
elif is_raining and not has_umbrella:
    print("Saya tidak bisa keluar karena hujan dan tidak punya payung.")
elif not is_raining and is_weekend:
    print("Cuaca baik, saatnya bersantai di akhir pekan!")
else:
    print("Hari biasa dan cuaca cerah, saatnya bekerja.")

# Contoh penggunaan operator logika dalam fungsi
def can_go_out(raining, weekend, umbrella):
    if not raining or (weekend and umbrella):
        return True
    return False

# Memeriksa apakah bisa keluar
if can_go_out(is_raining, is_weekend, has_umbrella):
    print("Saya bisa keluar!")
else:
    print("Saya tidak bisa keluar.")
