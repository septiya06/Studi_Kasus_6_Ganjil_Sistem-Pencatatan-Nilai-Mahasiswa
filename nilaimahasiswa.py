import json

path = r"D:\Python\StudiKasus6\nilaimahasiswa.json"

with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

def tambah_data(nama, nim, mata_kuliah, nilai):
    data.append({
        "nama": nama,
        "nim": nim,
        "mata_kuliah": mata_kuliah,
        "nilai": nilai
    })
    return "Data nilai berhasil ditambahkan!"

def simpan_file():
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    return "Data berhasil disimpan ke nilai_mahasiswa.json!"

while True:
    print("\n===== SISTEM PENCATATAN NILAI MAHASISWA =====")
    print("1. Lihat Histori Nilai")
    print("2. Tambah Nilai Mahasiswa")
    print("3. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        print("\n--- HISTORI NILAI MAHASISWA ---")

        if len(data) == 0:
            print("Belum ada data nilai.")
        else:
            for mahasiswa in data:
                print("Nama        :", mahasiswa["nama"])
                print("NIM         :", mahasiswa["nim"])
                print("Mata Kuliah :", mahasiswa["mata_kuliah"])
                print("Nilai       :", mahasiswa["nilai"])
                print("-----------------------------")

    elif pilihan == "2":
        print("\n--- TAMBAH NILAI MAHASISWA ---")

        nama = input("Masukkan nama mahasiswa: ")
        nim = input("Masukkan NIM: ")
        mata_kuliah = input("Masukkan mata kuliah: ")
        nilai = int(input("Masukkan nilai: "))

        print("\n", tambah_data(nama, nim, mata_kuliah, nilai))
        print(simpan_file())

    elif pilihan == "3":
        print("\nProgram selesai.")
        break

    else:
        print("\nPilihan tidak tersedia.")