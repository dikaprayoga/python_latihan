#dikerjakan oleh dika prayoga gunawan
#tanggal pengerjaan 22 oktober 2024
#program menghitung tabung

print("="*20)
print("tabung")
print("="*20)

jari = float(input("Masukan Jari-jari : "))
tinggi = float(input("Masukan Tinggi : "))
volume = 2 * 3.14 * jari * tinggi 
luas = 3.14 * jari * jari + 2 * 3.14 * jari * tinggi

print(f'volume : {round (volume, 2)} cm3')
print(f'Luas : {round (luas, 2)} cm')