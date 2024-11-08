print('\n')
print('='*30)
print('kalkulator')
print('='*30)

angka1 = float(input('\nMasukan angka pertama : '))
operator = input('masukan operator (+,-,*,/): ')
angka2 = float(input('Masukan angka kedua : '))

if operator == '+' :
    print(angka1 + angka2)
elif operator == '-' :
    print(angka1 - angka2)
elif operator == '*' :
    print(angka1 * angka2)
elif operator == '/' :
    print(angka1 / angka2)