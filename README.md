# **README**
Ini adalah repositori untuk tugas PBP 2025 milik Daffa Desra Hastiar (2306165490) dari kelas PBP C.

Link aplikasi PWS : http://daffa-desra-findyourfits.pbp.cs.ui.ac.id/

## **TUGAS 2**
### 1) Jelaskan bagaimana cara kamu mengimplementasikan _checklist_ di atas secara _step-by-step_ (bukan hanya sekadar mengikuti tutorial)
1. **Pertama-tama, saya membuat folder lokal baru di laptop dengan nama `findyourfits`**. Setelah itu, saya membuat direktori lokal dengan nama yang sama yang kemudian saya inisiasi dengan Git. Di dalam folder tersebut, saya menambahkan file README.md pertama saya yang berisi identitas diri saya. 
2. **Kedua, saya membuat repositori Github baru bernama "findyourfits" pada akun Github saya.** Pada langkah ini, saya membuat branch utama saya yang saya namakan "main". Kemudian, saya menjalankan perintah `git remote add origin <URL_REPO_SAYA>` untuk menghubungkan repositori lokal saya dengan repositori di Github. Kemudian saya melakukan `add`,`commit`, dan `push` ke repositori saya untuk pertama kalinya.
3. **Ketiga, saya menginisiasi dan mengaktifkan _Virtual Enviroment_ pada folder `findyourfits` **. 
4. **Keempat, saya membuat berkas `requirements.txt` di dalam folder `findyourfits` yang berisi:
	```
	django  
	gunicorn  
	whitenoise  
	psycopg2-binary  
	requests  
	urllib3
	```
	yang kemudian saya install menggunakan command `pip install -r requirements.txt`. Setelah itu, saya membuat proyek baru dengan nama `findyourfits` dengan command:
	`django-admin startproject findyourfits .`
5. **Kelima, saya membuat berkas `.gitignore` dengan isi yang sesuai pada Tutorial 0.** Setelah itu, saya melakukan Git `add`, `commit`, dan `push` ke repositori Github `findyourfits`.
6. **Keenam, saya melakukan konfigurasi untuk project `findyourfits` pada Pacil Web Service (PWS)**. Pada langkah ini, saya menambahkan project `findyourfits` melalui website **Pacil Web Service (PWS)**. Setelah itu, saya menambahkan `ALLOWED_HOSTS` pada `settings.py` di proyek Django `findyourfits` seperti berikut:
`ALLOWED_HOSTS  = ["localhost", "127.0.0.1", "daffa-desra-findyourfits.pbp.cs.ui.ac.id"]`
Kemudian, saya mengubah nama branch utama menjadi `main` dengan perintah `git branch -M main`. Setelah itu, saya melakukan push ke repositori Github dan PWS.
7. **Ketujuh, saya membuat aplikasi `main` pada proyek `findyourfits`**. Kemudian, saya mendaftarkan aplikasi main ke dalam proyek `findmyfits` dengan cara menambahkan `main` pada berkas `settings.py` seperti berikut:
	```
	INSTALLED_APPS =  [  
	...,  
	'main'  
	]
	```
8. **Kedelapan, saya menambahkan berkas `main.html` ke dalam direktori baru bernama `templates` pada direktori aplikasi `main`**. Berikut adalah file `main.html` yang saya buat:
	```
	<h1>FindYourFits</h1>
	
	<h3>Nama Aplikasi </h3>
	<p>{{ app_name }}</p>
	<h3>Nama </h3>
	<p>{{ name }}</p>
	<h3>NPM </h3>
	<p>{{ name }}</p>
	<h3>Kelas </h3>
	<p>{{ class }}</p>
	```
9. **Kesembilan, menambahkan model `Product` ke dalam aplikasi  main.** Langkah ini saya lakukan dengan mengubah `models.py` yang ada di dalam folder `main` . Berikut adalah berkas models.py yang saya buat:
	```
	from  django.db  import  models

	# Create your models here.
	class  Product(models.Model):
		name  =  models.CharField(max_length=200)
		price  =  models.IntegerField()
		stock  =  models.IntegerField() # tambahan
		condition  =  models.TextField() # used or new
		description  =  models.TextField() # tambahan
	``` 
	Kemudian, saya membuat dan mengaplikasikan migrasi model dengan menjalankan kedua perintah berikut:
	```python manage.py makemigrations```
	```python manage.py migrate```
10. **Kesepuluh, saya melakukan konfigurasi routing URL Aplikasi `main`.** Pada langkah ini, saya menambahkan `urls.py` yang berisi:
	```
	from  django.urls  import  path
	from  main.views  import  show_main

	app_name  =  'main'
	urlpatterns  = [
		path('', show_main, name='show_main'),
	]
	```
11. **Kesebelas, saya melakukan konfigurasi routing URL Proyek**. Langkah ini saya lakukan dengan mengubah beberapa kode dalam berkas `urls.py` yang terletak di dalam direktori proyek `findyourfits`. Perubahan yang saya lakukan adalah menambahkan impor fungsi `include` dari `django.urls` dan menambahkan `path('',include('main.urls'))` dalam variabel `urlpatterns`.
12. **Keduabelas, saya melakukan testing apakah proyek Django yang saya buat sudah bisa berjalan sesuai dengan apa yang saya mau atau belum**. Langkah ini saya lakukan dengan menjalankan perintah `python manage.py runserver` pada terminal dan membuka http://localhost:8000/ pada web browser.
13. **Terakhir, saya melakukan commit dan push ke repositori Github dan ke Pacil Web Service (PWS)**



### 2) - Buatlah bagan yang berisi  _request client_  ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara  `urls.py`,  `views.py`,  `models.py`, dan berkas  `html`.
![PBP Tugas 2](https://github.com/user-attachments/assets/62d5de3e-d0b6-49c0-926f-cc6e32ae44d4)
Alur Proses:
1. User melakukan permintaan HTTP _(HTTP Request)_ berupa URL untuk meminta resource ke framework Django.
2. Framework Django mencari URL yang diminta user.
3. URL `(urls.py)` memanggil view yang sesuai dengan kode pada `views.py`.
4. View `(views.py)` akan berinteraksi dengan Model `(models.py`) untuk mengambil ataupun mengubah data dari database.
5. View `(views.py)` meng-_compile_ respons yang diberikan oleh Model `(models.py`) kembali ke Template `(template.html)`
6. Hasil akhirnya adalah respons HTTP _(HTTP Response)_ yang dikirim kembali ke user dalam bentuk _web page_ atau halaman HTML.
### 3) Jelaskan fungsi  `git`  dalam pengembangan perangkat lunak!
**Git** adalah sistem kontrol versi terdistribusi _(distributed version control)_ yang dirancang untuk melacak perubahan _source code_ selama pengembangan perangkat lunak.
**Git** memungkinkan banyak pengembang atau _developer_ untuk mengerjakan suatu proyek secara bersamaan tanpa mengganggu pekerjaans atu sama lain.
Beberapa **fitur utama** yang dimiliki **git** adalah:
1. **_Version Control_**: Git menyimpan riwayat perubahan file sehingga kita bisa saja kembali ke versi sebelumnya jika diperlukan.
2. **_Branching_ dan _Merging_**: Git memungkinkan _developer_ untuk membuat _branch_ atau cabang sehingga _developer_ bisa menambahkan fitur atau memperbaiki _bug_ secara independen. Ketika _developer_ sudah selesai, maka file atau kode yang sudah ditambahkan atau diubah pada suatu cabang bisa digabung _(merge)_ kembali ke basis kode utama _(main codebase)_
3. **Sistem Terdistribusi**: Setiap _developer_ memiliki _copy_ dari _repository_ termasuk riwayatnya dalam komputer mereka. Dengan demikian, pekerjaan _developer_ tidak terlalu bergantung terhadap server utama.
4. **Kolaborasi**: **Git** memfasilitasi kolaborasi antar-_developer_ sehingga mudah untuk membagikan perubahan, melakukan _review_ kode, dan melihat kontribusi terhadap kode.
5. **Efisiensi**: **Git** memiliki performa yang optimal, sehingga _developer_ dapat melakukan operasi seperti _commit_ perubahan, _branching_, dan _merging_ dengan cepat.
(Dikutip dari https://www.quora.com/What-is-Git-and-why-should-I-use-it)

### 4) Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Menurut beberapa sumber yang saya baca tentang framework Django, terdapat beberapa poin yang saya anggap sebagai alasan kenapa Django digunakan sebagai framework yang dipelajari dalam mata kuliah PBP ini, yaitu:
1. **Django dibuat menggunakan Python**, sehingga sintaksnya cukup familiar setidaknya bagi saya pribadi.
2. **Django menggunakan struktur MVT _(Model-View-Template)_** yang menurut saya cukup mudah untuk dipahami bagi orang yang belum pernah melakukan web-development sebelumnya seperti saya.
3. **Framework Django dapat diakses secara gratis dan bersifat _open source_**. Selain itu, Django memiliki dokumentasi yang luas dan mudah diikuti sehingga cocok untuk kegiatan pembelajaran.
4.  **Django digunakan oleh banyak perusahaan di dunia**, diantaranya adalah Instagram, Spotify, dan YouTube. Dengan demikian, _framework_ Django sudah terbukti pengaplikasiannya di dunia sehingga bisa dijadikan sebagai framework untuk kegiatan pembelajaran.
### 5) Mengapa model pada Django disebut sebagai  _ORM_?
Karena ORM _(Object Relational Mapping)_ melakukan mapping dengan tabel-tabel dalam database dengan objek-objek dalam Python. Untuk melakukan CRUD _(Create, Read, Update, and Delete)_ pada Django, kita tidak perlu menuliskan query SQL secara langsung, melainkan kita hanya perlu melakukan perubahan terhadap suatu objek Python dengan metode yang mewakili operasi pada database. 