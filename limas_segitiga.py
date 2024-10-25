# dibuat oleh dika prayoga gunawan
# tanggal pengerjaan 10 oktober 2024
# progam menghitung limas segitiga

print("="*40)
print("limas segitiga")
print("="*40)

la = float(input("Masukan luas alas limas : "))
t = float(input("Masukan tinggi limas : "))
st = float(input("Masukan luas sisi tegak limas : "))

lp = la + st
v = 1/3 * la * t

print(f'''Volume\t: {v}
Luas permukaas\t: {lp}
''')
