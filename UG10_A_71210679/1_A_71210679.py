UG = float(input("Masukkan nilai rata-rata UG anda: "))
TTS = float(input("Masukkan nilai TTS anda: "))
TAS = float(input("Masukkan nilai TAS anda: "))
print(30*"=")
Total= ((UG*70)/100)+((TTS*15)/100)+((TAS*15)/100)
if Total >= 85:
    Letter = "A"
elif Total >= 80:
    Letter = "-A"
elif Total >= 75:
    Letter = "B+"
elif Total >= 70:
    Letter = "B"
elif Total >= 65:
    Letter = "B-"
elif Total >= 60:
    Letter = "C+"
elif Total >= 55:
    Letter = "C"
elif Total >= 45:
    Letter = "D"
else: 
    Letter = "E"
print("Nilai anda:", Total)
print("Nilai huruf anda: ", Letter)