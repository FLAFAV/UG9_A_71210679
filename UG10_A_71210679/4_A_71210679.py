Article = input("Masukkan artikel yang ingin dipindai: ")
Club = input("Masukkan nama klub favorit anda: ")
Score = input("Masukkan skor yang ingin dicari: ")
if Score in Article and Club in Article:
    print("Hasil pencarian ditemukan")
elif Club in Article:
    print("Hanya kata {} yang ditemukan pada artikel ini".format(Club))
elif Score in Article:
    print("Hanya skor {} yang ditemukan pada artikel ini".format(Score))
else:
    print("Hasil pencarian {} dan {} tidak ditemukan".format(Club,Score))