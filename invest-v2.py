import random

def hitung_investasi(principal, return_rate, years, currency):
    investasi = principal
    for year in range(1, years + 1):
        investasi = investasi * (1 + return_rate)
    return investasi, currency

def berikan_saran(return_rate, currency):
    if return_rate > 0.1 and currency == "Kripto":
        return "Saran: Pertimbangkan untuk berinvestasi di perusahaan Kripto X karena tingkat pengembalian tahunannya tinggi."
    elif return_rate > 0.05 and currency == "IDR":
        return "Saran: Pertimbangkan untuk berinvestasi di perusahaan IDR Y karena tingkat pengembalian tahunannya tinggi."
    else:
        return "Saran: Pertimbangkan untuk melakukan riset lebih lanjut sebelum berinvestasi."

def evaluasi_investasi(principal, hasil_investasi):
    if hasil_investasi > principal:
        return "Investasi Anda telah meningkat."
    elif hasil_investasi < principal:
        return "Investasi Anda telah menurun."
    else:
        return "Investasi Anda tetap sama."

def tampilkan_informasi():
    print("Program Investasi Sederhana")
    print("===========================")

def main():
    tampilkan_informasi()
    
    while True:
        print("\nPilihan Menu:")
        print("1. Hitung Investasi (Kripto)")
        print("2. Hitung Investasi (IDR)")
        print("3. Keluar")
        
        pilihan = input("Silakan pilih menu (1/2/3): ")
        
        if pilihan == "1":
            principal = float(input("Jumlah investasi awal (USD): "))
            return_rate = random.uniform(0.05, 0.15)
            years = int(input("Jangka waktu investasi (tahun): "))
            currency = "Kripto"
            
            hasil_investasi, currency = hitung_investasi(principal, return_rate, years, currency)
            print(f"\nSetelah {years} tahun, investasi Anda dalam {currency} akan menjadi ${hasil_investasi:.2f}")
            saran = berikan_saran(return_rate, currency)
            print(saran)
            evaluasi = evaluasi_investasi(principal, hasil_investasi)
            print(evaluasi)
        elif pilihan == "2":
            principal = float(input("Jumlah investasi awal (IDR): "))
            return_rate = random.uniform(0.03, 0.1)
            years = int(input("Jangka waktu investasi (tahun): "))
            currency = "IDR"
            
            hasil_investasi, currency = hitung_investasi(principal, return_rate, years, currency)
            print(f"\nSetelah {years} tahun, investasi Anda dalam {currency} akan menjadi {int(hasil_investasi)} {currency}")
            saran = berikan_saran(return_rate, currency)
            print(saran)
            evaluasi = evaluasi_investasi(principal, hasil_investasi)
            print(evaluasi)
        elif pilihan == "3":
            print("Terima kasih telah menggunakan program ini. Selamat investasi!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang benar.")

if __name__ == "__main__":
    main()
