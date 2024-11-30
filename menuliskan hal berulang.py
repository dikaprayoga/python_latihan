import os
os.system("cls")
print(30*"\033[92m=")
print("PROGRAM MENULIS BERULANG")
print(30*"\033[92m=")
print()

print(f"apa yang kamu fikir kan ?")
inputan = str(input("masukan jawaban anda = "))
if inputan == "dika":
    for i in range(1, 101):
        print(f"{i}.lupakan saja, dia bukan milikmu")
else:
    print(f"bagus, fikirkan saja {inputan}")