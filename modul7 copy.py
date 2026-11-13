def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    return a / b

while True:
    print("\n===== KALKULATOR =====")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    print("5. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua: "))
        print("Hasil:", tambah(a, b))
    elif pilihan == "2":
        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua: "))
        print("Hasil:", kurang(a, b))
    elif pilihan == "3":
        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua: "))
        print("Hasil:", kali(a, b))
    elif pilihan == "4":
        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua: "))
        print("Hasil:", bagi(a, b))
    elif pilihan == "5":
        print("Terima kasih telah menggunakan kalkulator.")
        break
