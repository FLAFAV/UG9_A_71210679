Input = input("Mendatar/menurun?: ")
if Input == "Mendatar":
    Symbol = "#"
    Quantity = int(input("Masukkan kolom: "))
    print(Symbol*Quantity)
elif Input == "Menurun":
    Symbol = "*"
    Quantity = int(input("Masukkan baris: "))
    print((Symbol + "\n")*Quantity)
else:
    print("Pola tidak dikenali")