print("="*30)
print("MENCARI NILAI")
print("="*30)
data_nilai = []
for i in range(3):
    data = int(input(f"masukan nilai {i+1} = "))
    data_nilai.append(data)
nilai_terbesar = data_nilai[0]
nilai_terkecil = data_nilai[0]

for i in data_nilai:
    if i > nilai_terbesar:
        nilai_terbesar = i
    elif i < nilai_terkecil:
        nilai_terkecil = i
print(f"nilai terbesar = {nilai_terbesar}")
print(f"nilai terkecil = {nilai_terkecil}")