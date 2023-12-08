# TUGAS-MATKUL-PBO-
Chindy Feby Amara (G1F022045)

## 1. Buatlah perulangan hingga 100 menggunakan Python dengan output sebagai berikut:
#### INPUT 
![image](https://github.com/chindyfebyamara/TUGAS-MATKUL-PBO-/assets/145527919/923fdd97-c90f-4496-b176-d6edf028d924)
#### PENJELASAN KODE
Kode Python di atas melakukan perulangan dari 1 hingga 100. Setiap kali nilai iterasi (i) adalah kelipatan 10, program akan mencetak teks "CHINDY FEBY AMARA" sebanyak 3 kali. Jika nilai iterasi tidak adalah kelipatan 10, maka nilai iterasi tersebut akan dicetak.
#### PENJELASAN SECTION KODE
1. For Loop Utama

>for i in range(1, 101):: Baris kode ini membuat loop utama yang akan beriterasi dari 1 hingga 100.

2. Pengecekan Kelipatan 10

>if i % 10 == 0:: Di dalam loop utama, kita memeriksa apakah nilai iterasi (i) merupakan kelipatan 10.

3. For Loop Dalam

>for _ in range(3):: Jika nilai iterasi merupakan kelipatan 10, kita masuk ke dalam loop tambahan yang akan mencetak "CHINDY FEBY AMARA" sebanyak 3 kali.

4. Cetak "CHINDY FEBY AMARA" atau Nilai Iterasi

>print("CHINDY FEBY AMARA"): Di dalam loop tambahan, kita mencetak string "CHINDY FEBY AMARA" sebanyak 3 kali jika nilai iterasi merupakan kelipatan 10.

>print(i): Jika nilai iterasi tidak merupakan kelipatan 10, kita mencetak nilai iterasi tersebut.
#### OUTPUT
![image](https://github.com/chindyfebyamara/TUGAS-MATKUL-PBO-/assets/145527919/e27c75ba-d73b-4fb8-acc3-e5e46ac52269)
## 2. Buatlah program bebas, dengan menerapkan if else pada: a. For Loops b. While Loops
### a. For Loops 
#### INPUT
![image](https://github.com/chindyfebyamara/TUGAS-MATKUL-PBO-/assets/145527919/c7d7b398-fb3a-41d1-9642-328d82de8de3)
#### PENJELASAN KODE
Program Menemukan Bilangan Prima Menggunakan For Loops
#### PENJELASAN SECTION KODE
1. For Loop Utama

>for num in range(2, 20): : Kode ini membuat loop utama yang mengiterasi dari 2 hingga 19, mencari bilangan prima dalam rentang ini.

2. Inisialisasi Flag Bilangan Prima

>is_prime = True : Variabel is_prime digunakan sebagai penanda untuk menentukan apakah suatu angka adalah bilangan prima.

3. For Loop Dalam untuk Memeriksa Bilangan Prima

>for i in range(2, int(num**0.5) + 1): : Loop ini digunakan untuk memeriksa apakah num adalah bilangan prima. Iterasi dimulai dari 2 hingga akar kuadrat dari num.

4. Pengecekan Bilangan Prima

>if num % i == 0: : Jika num dapat dibagi dengan i tanpa sisa, maka num bukan bilangan prima. Variabel is_prime diubah menjadi False dan loop dalam dihentikan menggunakan break.

5. Cetak Hasil

>if is_prime: : Jika is_prime masih True setelah loop dalam selesai, cetak bahwa num adalah bilangan prima.

>else: : Jika is_prime diubah menjadi False, cetak bahwa num bukan bilangan prima.

#### CARA KERJA
1. Loop utama mengiterasi dari 2 hingga 19.
2. Pada setiap iterasi, variabel is_prime diatur sebagai True.
3. Loop dalam kemudian memeriksa apakah num dapat dibagi oleh suatu angka (i).
4. Jika bisa, is_prime diubah menjadi False dan loop dalam dihentikan.
5. Setelah loop dalam selesai, program mengecek nilai is_prime dan mencetak apakah num adalah bilangan prima atau bukan.

Dengan cara ini, program mencetak status bilangan prima atau bukan untuk setiap angka dalam rentang 2 hingga 19. Anda dapat menjalankan program ini dan melihat hasilnya.
#### OUTPUT
![image](https://github.com/chindyfebyamara/TUGAS-MATKUL-PBO-/assets/145527919/a78b1c97-712d-4252-8fe3-bd1d9782f0cb)
### b. While Loops
#### INPUT
![image](https://github.com/chindyfebyamara/TUGAS-MATKUL-PBO-/assets/145527919/e5af8178-c93e-4838-908c-73314c52eee2)
#### PENJELASAN KODE
Program Menentukan Bilangan Ganjil atau Genap Menggunakan While Loops dan If Else
#### PENJELASAN SECTION KODE
1. Inisialisasi Variabel

>batas = 10: Variabel batas diinisialisasi dengan nilai 10, menentukan batas iterasi dalam program.
counter = 1: Variabel counter diinisialisasi dengan nilai 1, digunakan sebagai iterasi dalam while loop.

2. While Loop untuk Menentukan Bilangan Ganjil atau Genap

>while counter <= batas: : Kode ini menggunakan while loop untuk mengiterasi dari 1 hingga nilai yang ditentukan dalam variabel batas.

3. If Else untuk Menentukan Bilangan Ganjil atau Genap

>if counter % 2 == 0: : Pada setiap iterasi, program memeriksa apakah nilai counter habis dibagi 2 (genap) menggunakan operasi modulo (%).

>print(f"{counter} adalah bilangan genap"): Jika kondisi terpenuhi, program mencetak bahwa counter adalah bilangan genap.

>else: : Jika kondisi tidak terpenuhi (bilangan ganjil), program mencetak bahwa counter adalah bilangan ganjil.

4. Penambahan Counter

>counter += 1 : Setelah setiap iterasi, nilai counter ditambah 1 untuk melanjutkan ke iterasi selanjutnya.
#### CARA KERJA
1. Program menggunakan while loop untuk melakukan iterasi dari 1 hingga 10.
2. Pada setiap iterasi, program menggunakan if else untuk menentukan apakah nilai counter genap atau ganjil.
3. Hasilnya dicetak ke layar.
4. Setelah setiap iterasi, nilai counter ditingkatkan.
4. Program berhenti ketika counter melebihi nilai batas yang ditentukan.
Dengan cara ini, program mencetak status "bilangan genap" atau "bilangan ganjil" untuk setiap angka dari 1 hingga 10. Anda dapat menjalankan program ini dan melihat hasilnya.
#### OUTPUT
![image](https://github.com/chindyfebyamara/TUGAS-MATKUL-PBO-/assets/145527919/fcf06cd7-671c-42b3-8c10-98a75de7b946)

## 3. Buatlah sebuah variabel dengan tipe data array, kemudian tampilkan semua nilai dalam variabel tersebut menggunakan perulangan for
#### INPUT
![image](https://github.com/chindyfebyamara/TUGAS-MATKUL-PBO-/assets/145527919/314d1b76-8746-49ae-a34e-ee3e0bb67b72)
#### PENJELASAN KODE
program sederhana Python untuk membuat variabel dengan tipe data array (list) yang berisi nama-nama buah
#### PENJELASAN SECTION KODE
1. Membuat Variabel Array (List) dengan Nama Buah

>buah_list = ["Apel", "Jeruk", "Pisang", "Anggur", "Mangga"]: Variabel buah_list dibuat dan diinisialisasi dengan list yang berisi nama-nama buah.

2. For Loop untuk Menampilkan Nama Buah

>for buah in buah_list: : Kode ini menggunakan perulangan for untuk mengiterasi melalui setiap elemen (nama buah) dalam list buah_list.

3. Cetak Nama Buah

>print(buah): Setiap nama buah dicetak ke layar. Variabel buah akan memegang nilai dari setiap elemen dalam list selama iterasi.
#### CARA KERJA
1. Program pertama-tama membuat variabel buah_list yang berisi list nama-nama buah.
2. Kemudian, perulangan for digunakan untuk mengiterasi melalui setiap elemen dalam list buah_list.
3. Pada setiap iterasi, nilai dari elemen saat ini (nama buah) disimpan dalam variabel buah.
4. Nama buah kemudian dicetak ke layar menggunakan perintah print(buah).
Dengan cara ini, program mencetak setiap nama buah yang ada dalam list buah_list. Anda dapat menjalankan program ini dan melihat hasilnya
#### OUTPUT
![image](https://github.com/chindyfebyamara/TUGAS-MATKUL-PBO-/assets/145527919/7d43b8cc-cfe0-4ebf-8c6c-fc89be8542a1)


