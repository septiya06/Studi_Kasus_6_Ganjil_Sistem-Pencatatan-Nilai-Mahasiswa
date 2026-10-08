# Studi_Kasus_6_Ganjil_Sistem-Pencatatan-Nilai-Mahasiswa

# NAMA  : SEPTIYA MAHARANI
# NIM    : 101

# PENJELASAN PROGRAM

Program yang dibuat merupakan **Sistem Pencatatan Nilai Mahasiswa**. Program ini digunakan untuk mencatat, menampilkan, dan menyimpan data nilai mahasiswa menggunakan file JSON sebagai tempat penyimpanan data.<br>

Program memiliki tiga pilihan menu, yaitu **Lihat Histori Nilai, Tambah Nilai Mahasiswa, dan Keluar**. Program akan terus berjalan menggunakan `while` sampai pengguna memilih menu Keluar.<br>

## Penjelasan Kode

**1.Import Library JSON**<br>
  > <img width="95" height="28" alt="import json" src="https://github.com/user-attachments/assets/6cdd86a9-1b38-4b5b-9cc9-7c6de8c95d65" />

  **import json** digunakan untuk mengimpor library `json` yang digunakan untuk membaca dan menyimpan data dalam format JSON.<br>

**2.Menentukan Lokasi File JSON**<br>
> <img width="313" height="32" alt="path" src="https://github.com/user-attachments/assets/09ec08fa-7fd5-438d-91e7-3c4968d732a0" />

   **path = r"D:\Python\StudiKasus6\nilaimahasiswa.json"** Digunakan untuk menentukan lokasi file JSON yang digunakan oleh program. File `nilaimahasiswa.json` diletakkan di dalam folder `D:\Python\StudiKasus6` sebagai tempat penyimpanan data nilai mahasiswa.<br>

3. **`with open(path, "r", encoding="utf-8") as f:`**<br>
   Digunakan untuk membuka file JSON berdasarkan lokasi yang sudah ditentukan pada `path`. Mode `"r"` digunakan untuk membaca isi file, sedangkan `encoding="utf-8"` digunakan agar karakter dalam file dapat dibaca dengan baik.<br>

5. **`data = json.load(f)`**<br>
   Digunakan untuk membaca isi file JSON dan memasukkan data yang sudah tersimpan ke dalam variabel `data` sehingga data tersebut dapat digunakan oleh program.<br>

6. **`def tambah_data(nama, nim, mata_kuliah, nilai):`**<br>
   Digunakan untuk membuat function `tambah_data()` yang berfungsi untuk menambahkan data nilai mahasiswa baru. Function ini menerima data berupa **nama, NIM, mata kuliah, dan nilai**.<br>

7. **`data.append({...})`**<br>
   Digunakan untuk menambahkan data mahasiswa baru ke dalam list `data`. Data yang ditambahkan terdiri dari **nama, NIM, mata kuliah, dan nilai** sesuai dengan data yang dimasukkan oleh pengguna.<br>

8. **`return "Data nilai berhasil ditambahkan!"`**<br>
   Digunakan untuk mengembalikan pesan bahwa data nilai mahasiswa berhasil ditambahkan ke dalam `data`.<br>

9. **`def simpan_file():`**<br>
   Digunakan untuk membuat function `simpan_file()` yang berfungsi untuk menyimpan data nilai mahasiswa ke dalam file JSON secara permanen.<br>

10. **`with open(path, "w", encoding="utf-8") as f:`**<br>
   Digunakan untuk membuka file JSON berdasarkan lokasi pada `path`. Mode `"w"` digunakan untuk menulis atau menyimpan data ke dalam file JSON.<br>

11. **`json.dump(data, f, indent=4)`**<br>
    Digunakan untuk menyimpan seluruh data yang terdapat pada variabel `data` ke dalam file JSON. `indent=4` digunakan agar data yang tersimpan di dalam file JSON tersusun lebih rapi.<br>

12. **`return "Data berhasil disimpan ke nilai_mahasiswa.json!"`**<br>
    Digunakan untuk mengembalikan pesan bahwa data berhasil disimpan ke dalam file JSON.<br>

13. **`while True:`**<br>
    Digunakan untuk membuat program terus berjalan dan menampilkan menu secara berulang sampai pengguna memilih menu Keluar.<br>

14. **`print("\n===== SISTEM PENCATATAN NILAI MAHASISWA =====")`**<br>
    Digunakan untuk menampilkan judul utama program **Sistem Pencatatan Nilai Mahasiswa**.<br>

15. **`print("1. Lihat Histori Nilai")`**<br>
    Digunakan untuk menampilkan pilihan menu untuk melihat seluruh histori nilai mahasiswa yang sudah tersimpan.<br>

16. **`print("2. Tambah Nilai Mahasiswa")`**<br>
    Digunakan untuk menampilkan pilihan menu untuk menambahkan data nilai mahasiswa baru.<br>

17. **`print("3. Keluar")`**<br>
    Digunakan untuk menampilkan pilihan menu untuk keluar dari program.<br>

18. **`pilihan = input("Pilih menu: ")`**<br>
    Digunakan untuk meminta pengguna memasukkan pilihan menu. Pilihan yang dimasukkan akan disimpan ke dalam variabel `pilihan`.<br>

19. **`if pilihan == "1":`**<br>
    Digunakan untuk mengecek apakah pengguna memilih menu **Lihat Histori Nilai**.<br>

20. **`print("\n--- HISTORI NILAI MAHASISWA ---")`**<br>
    Digunakan untuk menampilkan judul bagian histori nilai mahasiswa.<br>

21. **`if len(data) == 0:`**<br>
    Digunakan untuk mengecek apakah data nilai mahasiswa yang terdapat dalam `data` masih kosong. `len(data)` digunakan untuk menghitung jumlah data yang tersedia.<br>

22. **`print("Belum ada data nilai.")`**<br>
    Digunakan untuk menampilkan pesan bahwa belum terdapat data nilai mahasiswa apabila jumlah data masih `0`.<br>

23. **`for mahasiswa in data:`**<br>
    Digunakan untuk mengambil dan membaca data mahasiswa satu per satu dari `data` agar seluruh histori nilai dapat ditampilkan.<br>

24. **`print("Nama        :", mahasiswa["nama"])`**<br>
    Digunakan untuk menampilkan nama mahasiswa berdasarkan data yang tersimpan pada bagian `"nama"`.<br>

25. **`print("NIM         :", mahasiswa["nim"])`**<br>
    Digunakan untuk menampilkan NIM mahasiswa berdasarkan data yang tersimpan pada bagian `"nim"`.<br>

26. **`print("Mata Kuliah :", mahasiswa["mata_kuliah"])`**<br>
    Digunakan untuk menampilkan mata kuliah mahasiswa berdasarkan data yang tersimpan pada bagian `"mata_kuliah"`.<br>

27. **`print("Nilai       :", mahasiswa["nilai"])`**<br>
    Digunakan untuk menampilkan nilai mahasiswa berdasarkan data yang tersimpan pada bagian `"nilai"`.<br>

28. **`print("-----------------------------")`**<br>
    Digunakan untuk memberikan garis pemisah antara data mahasiswa yang satu dengan data mahasiswa lainnya agar tampilan lebih rapi dan mudah dibaca.<br>

29. **`elif pilihan == "2":`**<br>
    Digunakan untuk mengecek apakah pengguna memilih menu **Tambah Nilai Mahasiswa**.<br>

30. **`print("\n--- TAMBAH NILAI MAHASISWA ---")`**<br>
    Digunakan untuk menampilkan judul bagian penambahan data nilai mahasiswa.<br>

31. **`nama = input("Masukkan nama mahasiswa: ")`**<br>
    Digunakan untuk meminta pengguna memasukkan nama mahasiswa. Data yang dimasukkan disimpan ke dalam variabel `nama`.<br>

32. **`nim = input("Masukkan NIM: ")`**<br>
    Digunakan untuk meminta pengguna memasukkan NIM mahasiswa. Data yang dimasukkan disimpan ke dalam variabel `nim`.<br>

33. **`mata_kuliah = input("Masukkan mata kuliah: ")`**<br>
    Digunakan untuk meminta pengguna memasukkan nama mata kuliah. Data yang dimasukkan disimpan ke dalam variabel `mata_kuliah`.<br>

34. **`nilai = int(input("Masukkan nilai: "))`**<br>
    Digunakan untuk meminta pengguna memasukkan nilai mahasiswa. `int()` digunakan untuk mengubah nilai yang dimasukkan menjadi bilangan bulat sehingga nilai disimpan sebagai angka.<br>

35. **`print("\n", tambah_data(nama, nim, mata_kuliah, nilai))`**<br>
    Digunakan untuk memanggil function `tambah_data()` dengan mengirimkan data nama, NIM, mata kuliah, dan nilai yang sudah dimasukkan pengguna. Setelah data berhasil ditambahkan, program menampilkan pesan **Data nilai berhasil ditambahkan!**<br>

36. **`print(simpan_file())`**<br>
    Digunakan untuk memanggil function `simpan_file()` agar data yang sudah ditambahkan disimpan ke dalam file JSON secara permanen. Setelah berhasil disimpan, program menampilkan pesan bahwa data berhasil disimpan ke file JSON.<br>

37. **`elif pilihan == "3":`**<br>
    Digunakan untuk mengecek apakah pengguna memilih menu **Keluar**.<br>

38. **`print("\nProgram selesai.")`**<br>
    Digunakan untuk menampilkan pesan bahwa program telah selesai dijalankan.<br>

39. **`break`**<br>
    Digunakan untuk menghentikan perulangan `while True` sehingga program berhenti dan tidak kembali menampilkan menu.<br>

40. **`else:`**<br>
    Digunakan apabila pengguna memasukkan pilihan selain menu **1, 2, atau 3**.<br>

41. **`print("\nPilihan tidak tersedia.")`**<br>
    Digunakan untuk menampilkan pesan bahwa pilihan yang dimasukkan pengguna tidak tersedia. Setelah itu program kembali ke menu karena masih berada dalam perulangan `while True`.<br>


Dengan menggunakan file JSON, data nilai yang sudah ditambahkan akan **tetap tersimpan meskipun program ditutup dan dijalankan kembali**.<br>
