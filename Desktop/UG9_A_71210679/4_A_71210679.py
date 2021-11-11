#Doni membangun sebuah rumah makan. Ia membutuhkan seorang programmer yang dapat 
#membantunya membuat catatan pemesanan dan penghitung pengeluaran pelanggan. 
#Bantulah Doni untuk membuat program tersebut!
#Yang dijual:
#- Ikan bakar seharga 25.000
#- Es doger seharga 6.000
#- Rujak cingur seharga 8.000

print("=====MASUKKAN JUMLAH MAKANAN YANG DIPESAN=====")
a = int(input("IKAN BAKAR   Rp.25.000,00 : "))
b = int(input("ES DOGER     Rp.6000,00   : "))
c = int(input("RUJAK CINGUR Rp.8000,00   : "))
print("=====TOTAL=====")
x = a*25000
y = b*6000
z = c*8000
print("TOTAL IKAN BAKAR     : Rp", x)
print("TOTAL ES DOGER       : Rp", y)
print("TOTAL RUJAK CINGUR   : Rp", z)
print("Jumlah total biaya yang harus dibayar adalah Rp", x + y + z)