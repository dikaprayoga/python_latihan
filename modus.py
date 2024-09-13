x = int(input("Masukan nilai x : "))
hasil = x%2

if hasil >0:
    print("x harus angka genap")

elif hasil == 0 :
    print(f'''hasil {x} dibagi 2 yaitu {x%2}''')