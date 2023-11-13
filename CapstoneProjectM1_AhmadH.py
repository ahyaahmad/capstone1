# JCDS 0406 - Ahmad Husaini 
# Capstone Project 1 : Program Klasemen Pertandingan Sepakbola
club = [
    {
        'nama': 'JCDS',
        'menang': 20,
        'seri': 10,
        'kalah': 8,
        'poin': 70
    },
    {
        'nama': 'JCWD',
        'menang': 20,
        'seri': 13,
        'kalah': 5,
        'poin': 73
    },
    {
        'nama': 'JCDM',
        'menang': 13,
        'seri': 10,
        'kalah': 15,
        'poin': 49
    }
]

def tambah_club():
    nama = input("Masukkan nama club: ")
    menang = int(input("Masukkan jumlah kemenangan: "))
    seri = int(input("Masukkan jumlah seri: "))
    kalah = int(input("Masukkan jumlah kekalahan: "))
        
    # Menghitung jumlah poin
    poin = (menang * 3) + seri
    
    club.append({"nama": nama, "menang": menang, "seri": seri, "kalah": kalah, "poin": poin})
    print(f"Club {nama} berhasil ditambahkan.")

def baca_klasemen():
    if not club:
        print("Klasemen kosong.")
        return

    def bandingkan_poin(tim):
        return tim["poin"]

    klasemen = sorted(club, key=bandingkan_poin, reverse=True)
    print("\nKlasemen Sepakbola:")
    for i, tim in enumerate(klasemen, start=1):
        print(f"{i}. {tim['nama']} - Menang: {tim['menang']}, Seri: {tim['seri']}, Kalah: {tim['kalah']}, Poin: {tim['poin']}")

def update_klasemen():
    baca_klasemen()
    nama_tim = input("\nMasukkan nama tim yang ingin diupdate klasemennya: ")
    for tim in club:
        if tim["nama"] == nama_tim:
            tim["menang"] = int(input("Masukkan jumlah kemenangan baru: "))
            tim["seri"] = int(input("Masukkan jumlah seri baru: "))
            tim["kalah"] = int(input("Masukkan jumlah kekalahan baru: "))
            
            # Menghitung jumlah poin baru
            tim["poin"] = (tim["menang"] * 3) + tim["seri"]
            
            print(f"Klasemen tim {nama_tim} berhasil diupdate.")
            return
    print(f"Tim {nama_tim} tidak ditemukan.")

def hapus_club():
    baca_klasemen()
    nama_tim = input("\nMasukkan nama tim yang ingin dihapus: ")
    for tim in club:
        if tim["nama"] == nama_tim:
            club.remove(tim)
            print(f"Tim {nama_tim} berhasil dihapus dari klasemen.")
            return
    print(f"Tim {nama_tim} tidak ditemukan.")

while True:
    print("\nMenu:")
    print("1. Tambah Club")
    print("2. Baca Klasemen")
    print("3. Update Klasemen")
    print("4. Hapus Club")
    print("5. Keluar")

    pilihan = input("Pilih operasi (1/2/3/4/5): ")

    if pilihan == "1":
        tambah_club()
    elif pilihan == "2":
        baca_klasemen()
    elif pilihan == "3":
        update_klasemen()
    elif pilihan == "4":
        hapus_club()
    elif pilihan == "5":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih kembali.")
