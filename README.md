# Studi_Kasus_6_Ganjil_Sistem-Pencatatan-Nilai-Mahasiswa

# NAMA  : SEPTIYA MAHARANI
# NIM    : 101


## Sistem Pencatatan Nilai Mahasiswa

Program ini digunakan untuk mencatat dan menampilkan histori nilai mahasiswa menggunakan file JSON sebagai tempat penyimpanan data. Program dapat membaca data nilai yang sudah tersimpan, menambahkan data nilai mahasiswa baru, dan menyimpan data tersebut secara permanen.<br>

## Penjelasan Kode

**1.Import Library JSON**<br>
  > <img width="95" height="28" alt="import json" src="https://github.com/user-attachments/assets/7ba2cf5b-9a58-4711-af71-501d847c20f1" />

   `import json` digunakan untuk mengimpor library JSON yang diperlukan untuk membaca dan menyimpan data dalam file JSON.<br>

**2.Menentukan Lokasi File JSON**<br>
> <img width="313" height="32" alt="path" src="https://github.com/user-attachments/assets/7baa0b33-81a4-4b8b-a0a2-c8213b295b37" />

   `path = r"D:\Python\StudiKasus6\nilaimahasiswa.json"` digunakan untuk menentukan lokasi file JSON yang digunakan sebagai tempat penyimpanan data nilai mahasiswa. File `nilaimahasiswa.json` diletakkan di dalam folder `D:\Python\StudiKasus6`.<br>

**3.Membuka File JSON**<br>
> <img width="287" height="23" alt="with open" src="https://github.com/user-attachments/assets/f6a8de9d-eeca-4a09-8a8b-70b454b06820" />

   `with open(path, "r", encoding="utf-8") as f:` digunakan untuk membuka file JSON berdasarkan lokasi yang sudah ditentukan pada `path`. Mode `"r"` digunakan untuk membaca isi file, sedangkan `encoding="utf-8"` digunakan agar karakter dalam file dapat dibaca dengan baik.<br>

**4.Membaca Data JSON**<br>
> <img width="175" height="23" alt="open w" src="https://github.com/user-attachments/assets/5171d1d1-d86e-4eca-b4e0-e6957abd09d7" />

   `data = json.load(f)` digunakan untuk membaca isi file JSON dan memasukkan data yang sudah tersimpan ke dalam variabel `data` sehingga data dapat digunakan oleh program.<br>

**5.Membuat Function Tambah Data**<br>
> <img width="294" height="25" alt="def tambah data" src="https://github.com/user-attachments/assets/e69b13db-12f5-4519-b621-0352cabf8851" />

   `def tambah_data(nama, nim, mata_kuliah, nilai):` digunakan untuk membuat function `tambah_data()` yang berfungsi untuk menambahkan data nilai mahasiswa baru. Function ini menerima data berupa nama, NIM, mata kuliah, dan nilai.<br>

**6.Menambahkan Data ke Dalam List**<br>
> <img width="301" height="92" alt="apped" src="https://github.com/user-attachments/assets/8b17d6e8-2839-4c20-8c7e-52e923a11b9c" />

   `data.append({...})` digunakan untuk menambahkan data mahasiswa baru ke dalam list `data`. Data yang ditambahkan terdiri dari nama, NIM, mata kuliah, dan nilai mahasiswa.<br>

**7.Mengembalikan Pesan Data Berhasil Ditambahkan**<br>
> <img width="302" height="28" alt="return" src="https://github.com/user-attachments/assets/178c4aec-96c0-46ad-80b6-d86f54a361d9" />

   `return "Data nilai berhasil ditambahkan!"` digunakan untuk mengembalikan pesan bahwa data nilai mahasiswa berhasil ditambahkan ke dalam `data`.<br>

**8.Membuat Function Simpan File**<br>
> <img width="294" height="25" alt="def tambah data" src="https://github.com/user-attachments/assets/f792c2d3-0846-4c92-b044-e2d1c8303fcb" />

   `def simpan_file():` digunakan untuk membuat function `simpan_file()` yang berfungsi untuk menyimpan data nilai mahasiswa ke dalam file JSON secara permanen.<br>

**9.Membuka File dalam Mode Write**<br>
> <img width="329" height="19" alt="w" src="https://github.com/user-attachments/assets/4e28e960-af93-40ec-ac2a-37c3f5847c95" />

   `with open(path, "w", encoding="utf-8") as f:` digunakan untuk membuka file JSON berdasarkan lokasi pada `path`. Mode `"w"` digunakan untuk menulis atau menyimpan data ke dalam file JSON.<br>

**10.Menyimpan Data ke File JSON**<br>
> <img width="277" height="20" alt="r" src="https://github.com/user-attachments/assets/6b252e54-e19d-4f79-afaf-3a47c50a4379" />

  `json.dump(data, f, indent=4)` digunakan untuk menyimpan data yang terdapat pada variabel `data` ke dalam file JSON. `indent=4` digunakan agar data yang tersimpan di dalam file JSON tersusun lebih rapi.<br>

**11.Mengembalikan Pesan Penyimpanan**<br>
> <img width="373" height="22" alt="re" src="https://github.com/user-attachments/assets/c6021c00-829a-4958-b084-1f10f12f7122" />

  `return "Data berhasil disimpan ke nilai_mahasiswa.json!"` digunakan untuk mengembalikan pesan bahwa data berhasil disimpan ke dalam file JSON.<br>

**12.Membuat Perulangan Program**<br>
> <img width="98" height="23" alt="while " src="https://github.com/user-attachments/assets/658bafd4-5088-458d-b691-be300f5c262a" />

  `while True:` digunakan agar program terus berjalan dan menu dapat digunakan berulang kali sampai pengguna memilih menu Keluar.<br>

**13.Menampilkan Judul Program**<br>
> <img width="355" height="21" alt="print sistem" src="https://github.com/user-attachments/assets/05e6c397-aee8-49a5-9d5c-424cbf3690be" />

  `print("\n===== SISTEM PENCATATAN NILAI MAHASISWA =====")` digunakan untuk menampilkan judul utama dari program Sistem Pencatatan Nilai Mahasiswa.<br>

**14.Menampilkan Menu Lihat Histori Nilai**<br>
> <img width="214" height="20" alt="lihat history" src="https://github.com/user-attachments/assets/172d7bff-dfc4-42a7-870a-510649381834" />

 `print("1. Lihat Histori Nilai")` digunakan untuk menampilkan pilihan menu yang digunakan untuk melihat seluruh histori nilai mahasiswa yang sudah tersimpan.<br>

**15.Menampilkan Menu Tambah Nilai Mahasiswa**<br>
> <img width="213" height="20" alt="tambah nilai" src="https://github.com/user-attachments/assets/614106bf-596b-4410-bb4d-1572731bdc0e" />

   `print("2. Tambah Nilai Mahasiswa")` digunakan untuk menampilkan pilihan menu yang digunakan untuk menambahkan data nilai mahasiswa baru.<br>

**16.Menampilkan Menu Keluar**<br>
> <img width="131" height="20" alt="keluar" src="https://github.com/user-attachments/assets/ef5bd6dc-54f5-46d1-bd00-b75175d44a40" />

   `print("3. Keluar")` digunakan untuk menampilkan pilihan menu yang digunakan untuk keluar dari program.<br>

**17.Menerima Pilihan Menu**<br>
> <img width="216" height="20" alt="pilihan=" src="https://github.com/user-attachments/assets/1c16237b-d363-41a9-b086-0e815d6e5cf4" />

  `pilihan = input("Pilih menu: ")` digunakan untuk meminta pengguna memasukkan pilihan menu. Pilihan yang dimasukkan akan disimpan ke dalam variabel `pilihan`.<br>

**18.Memilih Menu Lihat Histori Nilai**<br>
> <img width="146" height="19" alt="if1" src="https://github.com/user-attachments/assets/056cfc41-79e9-44cb-8dc5-5433b5a31667" />

  `if pilihan == "1":` digunakan untuk menjalankan proses Lihat Histori Nilai ketika pengguna memilih menu nomor 1.<br>

**19.Menampilkan Judul Histori Nilai**<br>
> <img width="279" height="17" alt="print history" src="https://github.com/user-attachments/assets/dc06ee2e-1a52-4328-a1af-40fb9669c143" />

  `print("\n--- HISTORI NILAI MAHASISWA ---")` digunakan untuk menampilkan judul bagian histori nilai mahasiswa.<br>

**20.Mengecek Data Nilai Kosong**<br>
> <img width="149" height="17" alt="if len" src="https://github.com/user-attachments/assets/df7ad9be-6182-47c1-9706-ebf59463e23f" />

 `if len(data) == 0:` digunakan untuk mengecek apakah jumlah data yang terdapat dalam `data` adalah 0 atau belum terdapat data nilai mahasiswa.<br>

**21.Menampilkan Pesan Data Kosong**<br>
> <img width="217" height="22" alt="blm ada data" src="https://github.com/user-attachments/assets/b6ecd77d-6073-44b6-aac7-971611d58153" />

  `print("Belum ada data nilai.")` digunakan untuk menampilkan pesan bahwa belum terdapat data nilai mahasiswa jika data dalam `data` masih kosong.<br>

**22.Mengambil Data Mahasiswa**<br>
> <img width="166" height="29" alt="else" src="https://github.com/user-attachments/assets/8825bd26-0346-4303-900d-c2bb3b7408d7" />

 `for mahasiswa in data:` digunakan untuk mengambil data mahasiswa satu per satu dari `data` agar seluruh histori nilai dapat ditampilkan.<br>

**23.Menampilkan Nama Mahasiswa**<br>
> <img width="275" height="20" alt="nama" src="https://github.com/user-attachments/assets/0b700e8a-edb4-4665-8228-9704ce54f96e" />

  `print("Nama        :", mahasiswa["nama"])` digunakan untuk menampilkan nama mahasiswa berdasarkan data yang tersimpan pada bagian `"nama"`.<br>

**24.Menampilkan NIM Mahasiswa**<br>
> <img width="250" height="17" alt="nim" src="https://github.com/user-attachments/assets/e76a91d1-ae09-413f-8113-8079efc016b9" />

  `print("NIM         :", mahasiswa["nim"])` digunakan untuk menampilkan NIM mahasiswa berdasarkan data yang tersimpan pada bagian `"nim"`.<br>

**25.Menampilkan Mata Kuliah**<br>
> <img width="300" height="16" alt="mata kuliah" src="https://github.com/user-attachments/assets/2d1bc326-0e12-4421-b5f9-da76356fe927" />

  `print("Mata Kuliah :", mahasiswa["mata_kuliah"])` digunakan untuk menampilkan mata kuliah mahasiswa berdasarkan data yang tersimpan pada bagian `"mata_kuliah"`.<br>

**26.Menampilkan Nilai Mahasiswa**<br>
> <img width="277" height="17" alt="nilai" src="https://github.com/user-attachments/assets/2bf6f731-38a0-453c-a87f-b48e06751f46" />

  `print("Nilai       :", mahasiswa["nilai"])` digunakan untuk menampilkan nilai mahasiswa berdasarkan data yang tersimpan pada bagian `"nilai"`.<br>

**27.Memberikan Garis Pemisah**<br>
> <img width="245" height="19" alt="---" src="https://github.com/user-attachments/assets/1b43e195-9e33-4de8-b4bb-2129ea0b22c3" />

  `print("-----------------------------")` digunakan untuk memberikan garis pemisah antara data mahasiswa yang satu dengan data mahasiswa lainnya agar tampilan lebih rapi dan mudah dibaca.<br>

**28.Memilih Menu Tambah Nilai Mahasiswa**<br>
> <img width="138" height="21" alt="elif 2" src="https://github.com/user-attachments/assets/bb6b9a54-3dcb-4dd9-bb84-2215a644055a" />

  `elif pilihan == "2":` digunakan untuk menjalankan proses Tambah Nilai Mahasiswa ketika pengguna memilih menu nomor 2.<br>

**29.Menampilkan Judul Tambah Nilai**<br>
> <img width="283" height="25" alt="print" src="https://github.com/user-attachments/assets/f55b662b-a414-4589-8da3-bdebf50ea168" />

  `print("\n--- TAMBAH NILAI MAHASISWA ---")` digunakan untuk menampilkan judul bagian penambahan nilai mahasiswa.<br>

**30.Memasukkan Nama Mahasiswa**<br>
> <img width="259" height="17" alt="nama input" src="https://github.com/user-attachments/assets/d8871b4a-9390-4d9b-8f3a-282c63e4961f" />

  `nama = input("Masukkan nama mahasiswa: ")` digunakan untuk meminta pengguna memasukkan nama mahasiswa dan menyimpannya ke dalam variabel `nama`.<br>

**31.Memasukkan NIM Mahasiswa**<br>
> <img width="196" height="19" alt="nim input" src="https://github.com/user-attachments/assets/6b5ba80e-2b5b-449d-ba8f-a8151411cd5e" />

  `nim = input("Masukkan NIM: ")` digunakan untuk meminta pengguna memasukkan NIM mahasiswa dan menyimpannya ke dalam variabel `nim`.<br>

**32.Memasukkan Mata Kuliah**<br>
> <img width="282" height="18" alt="mata_kuliah" src="https://github.com/user-attachments/assets/2dfdc844-9082-4f4c-9a09-fe7e65b88dcc" />

  `mata_kuliah = input("Masukkan mata kuliah: ")` digunakan untuk meminta pengguna memasukkan nama mata kuliah dan menyimpannya ke dalam variabel `mata_kuliah`.<br>

**33.Memasukkan Nilai Mahasiswa**<br>
> <img width="249" height="19" alt="nilain int" src="https://github.com/user-attachments/assets/b5af3559-4024-4997-84c2-ebe60c34d4d7" />

  `nilai = int(input("Masukkan nilai: "))` digunakan untuk meminta pengguna memasukkan nilai mahasiswa. `int()` digunakan untuk mengubah nilai yang dimasukkan menjadi bilangan bulat sehingga nilai disimpan sebagai angka.<br>

**34.Menambahkan Data Nilai Mahasiswa**<br>
> <img width="344" height="20" alt="print tambah" src="https://github.com/user-attachments/assets/96a07362-497b-47c1-b2d8-8fa2b1fd8384" />

  `print("\n", tambah_data(nama, nim, mata_kuliah, nilai))` digunakan untuk memanggil function `tambah_data()` dengan mengirimkan data nama, NIM, mata kuliah, dan nilai yang sudah dimasukkan oleh pengguna. Setelah data berhasil ditambahkan, program menampilkan pesan bahwa data nilai berhasil ditambahkan.<br>

**35.Menyimpan Data Nilai**<br>
> <img width="135" height="17" alt="print simpan file" src="https://github.com/user-attachments/assets/0023ea03-d7d7-4d19-ba1d-64a87dec2988" />

  `print(simpan_file())` digunakan untuk memanggil function `simpan_file()` agar data yang sudah ditambahkan disimpan secara permanen ke dalam file JSON.<br>

**36.Memilih Menu Keluar**<br>
> <img width="140" height="20" alt="elif 3" src="https://github.com/user-attachments/assets/6ccc88bf-8a68-47b9-b6b2-24d57d4991f3" />

  `elif pilihan == "3":` digunakan untuk menjalankan proses keluar dari program ketika pengguna memilih menu nomor 3.<br>

**37.Menampilkan Pesan Program Selesai**<br>
> <img width="190" height="19" alt="print 2" src="https://github.com/user-attachments/assets/1363dfdc-17ef-4ce1-9b65-c407ea24855a" />

   `print("\nProgram selesai.")` digunakan untuk menampilkan pesan bahwa program telah selesai dijalankan.<br>

**38.Menghentikan Perulangan**<br>
> <img width="55" height="22" alt="break" src="https://github.com/user-attachments/assets/cfa6275c-a856-4f8d-a195-81295b00567a" />

  `break` digunakan untuk menghentikan perulangan `while True` sehingga program berhenti dan tidak kembali menampilkan menu.<br>

**40.Menangani Pilihan yang Tidak Tersedia**<br>
> <img width="52" height="20" alt="else2" src="https://github.com/user-attachments/assets/57766f0f-ef65-4aaf-a922-8125d0fc1ca8" />

  `else:` digunakan ketika pengguna memasukkan pilihan selain menu 1, 2, atau 3.<br>

**40.Menampilkan Pesan Pilihan Tidak Tersedia**<br>
> <img width="230" height="23" alt="pilihana tidak" src="https://github.com/user-attachments/assets/4af6a268-ca60-4448-988d-95adf1a4bbef" />

  `print("\nPilihan tidak tersedia.")` digunakan untuk memberi tahu pengguna bahwa pilihan yang dimasukkan tidak tersedia. Setelah itu program kembali ke menu karena masih berada di dalam perulangan `while True`.<br>

## Hasil Output

**1.Hasil jika memilih 1.Lihat Histori Nilai(Data Baru Belum ditambahkan)**<br>
> <img width="319" height="264" alt="pilih 1" src="https://github.com/user-attachments/assets/a50fd066-05d2-4631-a252-5a41894e90a0" />
**Hasil jika memilih 2.Tambah Nilai Mahasiswa**<br>
> <img width="394" height="290" alt="pilih 2" src="https://github.com/user-attachments/assets/3aba7d62-d833-4810-9197-5d80be639454" />

**2.Hasil Jika Memilih 3.Keluar**<br>
><img width="314" height="133" alt="pilih 3" src="https://github.com/user-attachments/assets/f3abff1f-b779-4604-be82-128644a4faab" />
**3.Hasil Jika Gagal Keluar/Pilihan tidak tersedia**<br>
> <img width="290" height="104" alt="4" src="https://github.com/user-attachments/assets/df13b889-51d8-466c-b872-9951cf2898e7" />

**4.Isi di Dalam JSON Sebelum ditambahkan Data Baru**<br>
> <img width="380" height="230" alt="sebelum" src="https://github.com/user-attachments/assets/3d6e1720-973b-423d-9c1f-0cbab59c11ba" />

**5.Isi didalam JSON Jika Berhasil menambahkan data Baru dan Masuk Kedalam JSON**
> <img width="374" height="323" alt="json" src="https://github.com/user-attachments/assets/d03cb3c1-33b8-45d3-bfbc-2a86e34731e2" />

**6.Hasil jika memilih 1.Lihat Histori Nilai(Data Baru sudah ditambahkan)**<br>
> <img width="334" height="389" alt="setelah ditambahkan" src="https://github.com/user-attachments/assets/f58992fa-33df-4530-b9c0-4079e855199d" />









