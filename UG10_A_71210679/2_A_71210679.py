Hashtag = (28*"#")
print(Hashtag)
print("Kalkulator Advance Sederhana")
print(Hashtag)
print("1. Menghitung sisa hasil bagi")
print("2. Membulatkan kebawah hasil pembagian")
print("3. Mencari akar kubik sebuah bilangan")
Menu = int(input("Masukkan menu yang anda pilih: "))

if Menu == 1:
    Numerator = float(input("Masukkan bilangan yang ingin dibagi: "))
    Denominator = float(input("Masukkan bilangan pembagi: "))
    Results = (Numerator % Denominator)
    print("Sisa hasil bagi", Numerator, "dibagi dengan", Denominator, "adalah", Results)
elif Menu == 2:
    Numerator = float(input("Masukkan bilangan yang ingin dibagi: "))
    Denominator = float(input("Masukkan bilangan pembagi: "))
    Results = (Numerator // Denominator)
    print("Hasil pembagian", Numerator, "dibagi dengan", Denominator, "adalah", Results)
else:
    Data = float(input("Masukkan bilangan yang ingin dicari akar kubiknya: "))
    Results = (Data**(1/2))
    print("Akar kubik dari", Data, "Adalah", Results)