# dibuat oleh dika prayoga gunawan
# tanggal pengerjaan 10 oktober 2024
# progam menghitung lingkaran

print("="*40)
print("lingaran")
print("="*40)

r = int(input("masukan jarijari: "))

l =lambda r : 3.14 * r * r
k =lambda r : 2*3.14 * r

print("luas :",l(r),'cm2')
print("keliling :",round(k(r),2), 'cm2')
