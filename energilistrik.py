import os
os.system("cls")

print("="*20)
print("Energi Listrik")
print("="*20)

q = int(input("Muatan Listrik"))
v = int(input("Potensial Listrik"))
l = int(input("Kuat Arus Listrik"))
r = int(input("Hambatan: "))
t = int(input("Waktu: "))

epl = q * v

eldr = 1 * 1 * r * t

print(f"Energi Potensial Liar: {epl}")
print(f"Energi Listrik Dalam Rangkai: {epl}")
