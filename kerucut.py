#dikerjakan oleh dika prayoga gunawan
#tanggal pengerjaan 22 oktober 2024
#program menghitung rumus kerucut

print("="*20)
print("Rumus kerucut")
print("="*20)

r = int(input("Jari-jari\t: "))
s = int(input("Gsris Pelukis\t: "))
t = int(input("Tinggi\t\t: ")) 

lp = 3.14 * r * (r + s)
ls = 3.14 * r * s
v = 1/3 * 3.14 * 3.13 * r * r * t

print(f"Luas permukaan\t: {lp}")
print(f"Luas Selimut\t: {ls}")
print(f"volume\t\t: {v}")