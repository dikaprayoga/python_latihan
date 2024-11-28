print("="*30)
print("PROGRAM MENGHITUNG ANGKA GANJIL".center(30))
print("="*30)

angka = int(input("masukan angka = "))
jumlah_hasil = 0
for i in range(1, angka + 1):
    if i % 2 != 0:
        jumlah_hasil += i
print(f"hasilnya adalah = {jumlah_hasil}")
# print(f"angka ganjilnya saja = {hasil}")