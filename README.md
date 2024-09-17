# **README**
Ini adalah repositori untuk tugas PBP 2025 milik Daffa Desra Hastiar (2306165490) dari kelas PBP C.

Link aplikasi PWS : http://daffa-desra-findyourfits.pbp.cs.ui.ac.id/

## **TUGAS 3**
### 1. Jelaskan mengapa kita memerlukan  _data delivery_  dalam pengimplementasian sebuah platform?
Menurut beberapa sumber yang saya baca, _data platform_ penting dalam pengimplementasian sebuah platform karena _data delivery_ memungkinkan platform untuk menjalankan fungsi-fungsi yang melibatkan komunikasi antara komponen maupun user.

**Contoh _data delivery_** antara komponen dengan user dalam konteks tugas kali ini adalah ketika user ingin melihat produk apa saja yang ada di _e-commerce_. Untuk menampilkan produk-produk tersebut ke user, maka platform melakukan **_data delivery_** misalnya dari suatu database produk ke program front-end yang nantinya akan ditampilkan ke user.  

Contoh fungsi lain dari **_data delivery_** dalam kehidupan kita sehari-hari adalah ketika kita melakukan _search_ pada suatu sosial media misalkan _Instagram_. Ketika kita melakukan _search_, maka platform akan berkomunikasi dan melakukan _data delivery_ untuk memunculkan informasi atau data yang dicari oleh user.

Kesimpulannya adalah bahwa **platform memerlukan komunikasi diantara komponen-komponennya untuk melakukan fungsi-fungsinya.** Contoh komunikasi tersebut misalnya  komunikasi antara database dengan program back-end suatu platform. Komunikasi tersebut dapat dilakukan dengan adanya **_data delivery_**. Dengan demikian, suatu platform tidak akan berguna jika kita tidak menerapkan _data delivery_ dalam platform tersebut.
### 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Dari beberapa sumber yang saya baca di internet, terdapat beberapa kelebihan dari JSON dibandingkan dengan XML yang menyebabkan JSON menjadi format data yang lebih populer dibanding dengan XML. Berikut adalah beberapa kelebihan JSON dibandingkan dengan XML:
+ JSON bisa menampung _value_ berupa Integer, String, List, dan Array secara langsung. Sementara untuk tipe data yang serupa, **XML memerlukan _parsing_** dari String ke tipe data yang diinginkan.
+ **JSON memiliki sintaks yang lebih pendek dibandingkan XML**, sehingga JSON memiliki ukuran yang lebih kecil dan dapat dibaca ataupun ditulis dengan lebih cepat dibandingkan dengan XML. 
+ **JSON memiliki sintaks yang lebih mmudah untuk dibaca dibandingkan dengan XML**
+ **JSON didukung secara langsung oleh bahasa JavaScript** sehingga lebih mudah untuk terintegrasi dengan aplikasi pada JavaScript dan API.
+ **JSON lebih mudah untuk diparsing dibandingkan dengan XML** sehingga lebih cepat dan efisien ketika dijalankan.

Kesimpulanya adalah bahwa JSON lebih cocok untuk digunakan sebagai format data dalam pengembangan suatu website ataupun aplikasi karena JSON memiliki kecepatan dan efisiensi yang lebih baik dibandingkan dengan XML. Selain itu, JSON juga didukung langsung oleh JavaScript sehingga operasi-operasi dalam data JSON dapat dilakukan dengan lebih efisien dibandingkan dengan menggunakan XML yang harus diparsing terlebih dahulu. 
Dikarenakan dalam penggunaan web dan aplikasi banyak terjadi _data delivery_, maka saya memilih **JSON** sebagai format data yang **lebih baik** dibandingkan XML karena **JSON memakan ruang penyimpanan yang lebih kecil, dapat dijalankan dengan lebih efisien dan lebih mudah untuk dibaca dibandingkan dengan XML.**
### 3. Jelaskan fungsi dari method  `is_valid()`  pada form Django dan mengapa kita membutuhkan method tersebut?
Fungsi method `is_valid()` adalah untuk melakukan validasi pada _forms_ sehingga data yang dimasukkan memenuhi kriteria yang sudah ditentukan dalam _form fields_. 

Method `is_valid()` mengecek apakah data yang dimasukkan sudah sesuai dengan aturan-aturan yang kita tuliskan pada _form fields_, misalnya seperti **field mana saja yang harus diisi, tipe data apa yang digunakan pada suatu variabel, dan aturan validasi lainnya seperti nilai maksimum atau panjang string minimum.**  

Jika data valid, maka method `is_valid()` 
mereturn `True` dan akan mengisi dictionary `cleaned_data` yang berisi data yang sudah divalidasi dan dikonversi ke tipe data yang sesuai. 

Jika data tidak valid, maka method `is_valid()`  akan mereturn `False` dan kesalahan validasi tersebut akan disimpan dalam atribut `form.errors` sehingga kita bisa melihat kesalahan apa yang terjadi pada data yang tidak valid tersebut.

Menurut saya, method `is_valid()` dibutuhkan karena method tersebut dapat mencegah program untuk memasukkan data yang tidak benar sehingga error-error yang diakibatkan oleh kesalahan input dalam database dapat dihindari. Selain itu, method `is_valid()` juga dapat memastikan bahwa semua nilai dalam data yang kita miliki memang sudah benar dan siap untuk diproses oleh program selanjutnya.
### 4. Mengapa kita membutuhkan  `csrf_token`  saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan  `csrf_token`  pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
`csrf_token` adalah **random token yang berfungsi untuk mencegah _Cross-Site Request Forgery Attack_**. Adanya `csrf_token` menambah proteksi terhadap forms yang disubmit oleh user agar tidak dieksploitasi oleh penyerang melalui serangan CSRF.

Kode `{% csrf_token %}`ketika kita membuat suatu form, maka program akan membuat suatu _field_ tersembunyi yang memuat suatu token yang sulit untuk ditebak. Ketika form tersebut di-_submit_, maka Django akan memeriksa apakah token yang ada dalam form sesuai dengan yang tersimpan pada sesi user. Jika token tersebut match, maka request user akan dilanjutkan atau diterima.

Jika kita tidak menggunakan `csrf_token` pada forms yang kita buat, maka seorang _hacker_ bisa saja mengeksploitasi celah tersebut dengan melakukan  _Cross-Site Request Forgery (CSRF) Attack_. CSRF terjadi ketika seorang user _logged in_ ke website Django yang kita buat. _Hacker_ nantinya akan mengirimkan link website yang jika di klik oleh user, maka link tersebut akan mengirimkan request (seperti request untuk ganti password atau melakukan transfer uang) ke website Django kita tanpa interaksi dan tanpa sepengetahuan user. Karena user sudah terautentikasi dengan website Django kita, maka request yang dikirim oleh _hacker_ tersebut akan di-_treat_ seakan request tersebut dikirim oleh user. Tanpa adanya `csrf_token`, maka Django tidak akan tahu apakah request tersebut datang dari user atau bukan. Dengan demikian, request tersebut diteruskan sehingga terjadilah CSRF Attack.

### 5. Jelaskan bagaimana cara kamu mengimplementasikan  _checklist_  di atas secara  _step-by-step_  (bukan hanya sekadar mengikuti tutorial)