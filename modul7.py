nilai = [80,75,90,60,85]

def hitung_rata_rata(daftar_nilai):
    total = 0
    jumlah = 0

    for i in daftar_nilai:
        total += i
        jumlah += 1
    kalkulasi = total/jumlah

    return kalkulasi, total, jumlah

print(hitung_rata_rata(nilai))

# sebelumnya pada baris ke 8, saya menggunakan total += nilai[0]
# dan itu menyebabkan sedikit bug, karena hasil akhirnya adalah (80.0, 400, 5), yang di mana salah perhitungan.
# saya tanya chatgpt, dan dia menyarankan untuk menggunakan total += i, karena i akan mengambil setiap nilai dari daftar_nilai secara berurutan, sehingga hasil akhirnya menjadi (78.0, 390, 5), yang mana sudah benar.

a = ["Mangga", "Apel", "Jeruk", "Pisang", "Anggur"]

def cari_data(koleksi, data_dicari):
    for i in koleksi:
        if i == data_dicari:
            ada = True
            print(f"{data_dicari} ditemukan")
            return ada
        elif i != data_dicari and i != a:
            ada = False
            print(f"{data_dicari} tidak ditemukan")
            return ada
        
cari_data(a, "Apel")

#asoyyyy bisa gueh cuy, kalo logika nya dibantu dijabarkan sama A.I. MAN I SO BAD AT UNDERSTANDING THE QUESTION, FUCK! LOL

data = ["Mangga", "Apel"]

def tambah_data(list_lama, data_baru):
    data_baru = list_lama + [data_baru]
    return data_baru

print(tambah_data(data, "Jeruk"))
