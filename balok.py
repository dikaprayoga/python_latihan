# dibuat oleh dika prayoga gunawan
# tanggal pengerjaan 10 oktober 2024
# progam menghitung balok

print("="*40)
print("balok")
print("="*40)

p = int(input("panjang\t\t: "))
l = int(input("Lebar\t\t: "))
t = int(input("Tinggi\t\t: "))

lp = 2 * (p * l + p * t + l * t)
v = p * l * t
l = 4 * (p + l + t)

print(f"Luas Permukaan\t: {lp}")
print(f"Volume\t\t: {v}")
print(f"Keliling\t: {l}")
