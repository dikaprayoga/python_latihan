import os
os.system("cls")
print(30*"\033[92m=")
print("PROGRAM MENGHITUNG ANGKA GANJIL".center(30))
print(30*"\033[92m=")

angka = int(input("masukan angka = "))
jumlah_hasil = 0
for i in range(1, angka + 1):
    if i % 2 != 0:
        jumlah_hasil += i
print(f"hasilnya adalah = {jumlah_hasil}")
# print(f"angka ganjilnya saja = {hasil}")